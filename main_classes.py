import pathlib
import sys
from json import load, dump

import keyboard
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import (
    QApplication
)
from loguru import logger

import classes
from UIs import settings
from classes.WindowCloser import WindowCloser
from public_functions import *

__all__ = ["MainWindow"]


# noinspection PyAttributeOutsideInit
class MainWindow(classes.basic_classes.MyQWidget.MyQWidget):
    """
    自定义主窗口类
    """

    # 定义应用信号
    apply_signal = Signal()
    state_changed_signal = Signal()
    hide_window_signal = Signal()

    @logger.catch
    def __init__(self, app: QApplication):
        QApplication.processEvents()
        super().__init__()
        self.app = app
        # 初始化ui
        self.ui = settings.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("那刻夏")
        set_window_size(self, app)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_PaintOnScreen)
        # 实例化关闭窗口类
        self.window_closer = WindowCloser()
        # 初始化日志管理类
        self.logger_manager = classes.LogManager(self)
        # 软件激活状态
        self.state: bool = True
        # 默认配置文件
        # noinspection SpellCheckingInspection
        self.default_config: dict = {
            "hide_tray": 0,
            "forKillExe": [
                "EXCEL.Title",
                "EasiCamera.exe",
                "POWERPNT.Title",
                "WINWORD.Title",
                "et.exe",
                "wps.exe",
                "wpscloudsvr.exe",
            ],
            "forKillWindowTitle": [
                ".pdf",
                ".ppt",
                ".pptx",
                ".xlsx",
                "192.168.",
                "\u5206\u4eab\u7684\u56fe\u7247",
                "\u6587\u6863\u6587\u4ef6",
                "\u804a\u5929\u8bb0\u5f55",
            ],
            "random_time": [0, 30],
            "hold_time": 0,
        }
        # 持续时间
        self.hold_time: int = 0
        # 下课时间表
        self.time_config: dict = {}
        # 软件生命状态
        self.life: bool = True
        # 测试模式
        self.test: bool = False
        # 隐藏托盘图标
        self.hide_tray: int = self.default_config["hide_tray"]
        # 待杀程序列表
        self.forKillExe: list[str] = self.default_config["forKillExe"]
        # 待杀应用窗口标题
        self.forKillWindowTitle: list[str] = self.default_config["forKillWindowTitle"]
        # 随机等待时间
        self.random_time: list[int] = self.default_config["random_time"]
        # 配置文件路径
        self.clock_json_path: str = pathlib.PurePath.joinpath(
            pathlib.Path(sys.argv[0]).resolve().parent, "clock.json"
        ).__str__()
        self.config_json_path: str = pathlib.PurePath.joinpath(
            pathlib.Path(sys.argv[0]).resolve().parent, "config.json"
        ).__str__()
        logger.debug(f"配置文件路径: {self.clock_json_path}")
        logger.debug(f"配置文件路径: {self.config_json_path}")
        QShortcut(QKeySequence("Alt+A"), self).activated.connect(
            lambda: (
                self.flash_state_changed() if self.ui.apply_button.isEnabled() else None
            )
        )
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.quit_app)
        # region 初始化时间列表管理器
        self.time_manager = classes.TimeManager(self)
        # endregion
        # region 初始化热键管理器
        self.hot_key_manager = classes.HotKeyManager(self)
        self.hot_key_manager.show_window_signal.connect(self.show_window)
        # endregion
        # region 处理配置文件
        t = 0
        try:
            with open(self.clock_json_path, encoding="utf-8") as f:
                self.time_config = load(f)
                logger.debug(f"下课时间配置: {self.time_config}")
            t = 1
            with open(self.config_json_path, encoding="utf-8") as f:
                self.load_config(load(f))
                logger.debug("导入成功")
        except Exception as e:
            if t == 0:
                logger.error(f"时间表配置文件不存在或损坏, 创建默认时间表配置文件{e}")
                with open(self.clock_json_path, "w") as f:
                    dump({"00:00": "Default Description"}, f, indent=4)
                logger.critical(f"严重未知错误, 错误代码: {e}")
            elif t == 1:
                logger.error(f"功能配置文件不存在或损坏, 创建默认配置文件{e}")
                with open(self.config_json_path, "w") as f:
                    dump(self.default_config, f, indent=4)
            else:
                logger.critical(f"严重未知错误, 错误代码: {e}")
                sys.exit(1)
        self.show_config()
        # endregion
        # region 刷新控件状态
        self.ui.if_tray_hide.setChecked(bool(self.hide_tray))
        self.ui.if_strong_hide.setChecked(self.hide_tray == 2)
        self.ui.if_tray_hide.setDisabled(self.ui.if_strong_hide.isChecked())
        self.ui.a.setValue(self.random_time[0])
        self.ui.b.setValue(self.random_time[1])
        self.ui.hold_seconds.setValue(self.hold_time)
        # endregion
        # region 关联控件函数
        normal_widgets: list = [
            self.ui.if_tray_hide,
            self.ui.if_strong_hide,
            self.ui.a,
            self.ui.b,
            self.ui.hold_seconds,
        ]
        connect_signals(normal_widgets, self.set_flushable)
        self.ui.apply_button.clicked.connect(self.flash_state_changed)
        self.ui.is_active.clicked.connect(self.state_changed_signal.emit)
        self.ui.test_button.clicked.connect(self.testing)
        self.ui.exit_button.clicked.connect(self.quit_app)
        self.ui.if_strong_hide.stateChanged.connect(self.strong_hide_action)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)
        # endregion
        # region 时间点编辑功能实现
        # 检测时间列表选中项改变和描述内容改变
        self.ui.time_list.itemSelectionChanged.connect(
            self.time_manager.flash_description
        )
        self.ui.description.textChanged.connect(self.time_manager.edit_description)
        self.ui.time_list.addItems(list(sorted(self.time_config.keys())))
        # endregion

        # region 初始化托盘图标
        self.tray_icon = classes.Tray(self)
        self.tray_icon.flash_tray()
        # endregion

        # region 初始化待杀应用窗口类
        self.add_executable = classes.EXE.AddEXE.AddEXE(self)
        self.edit_executable = classes.EXE.EditEXE.EditEXE(self)
        # endregion

        # region 初始化待杀窗口标题类
        self.add_title = classes.Title.AddTitle.AddTitle(self)
        self.edit_title = classes.Title.EditTitle.EditTitle(self)
        # endregion

        # region 初始化消息提示类
        self.warner = classes.MessageShower(self, self.tray_icon)
        # endregion

        # region 初始化待杀程序列表
        self.ui.for_kill_list.addItems(self.forKillExe)
        self.ui.for_close_title.addItems(self.forKillWindowTitle)
        logger.debug("已加载待杀程序列表")
        # endregion

    # region 主窗口类方法s
    @logger.catch
    def strong_hide_action(self, state):
        """
        关联强隐藏托盘图标
        :return:
        """
        self.ui.if_tray_hide.setDisabled(state)
        self.ui.if_tray_hide.setChecked(True)

    @logger.catch
    def testing(self):
        self.test = True

    @logger.catch
    def set_flushable(self, *args, **kwargs):
        """
        设置应用按钮为可点击状态
        :return:
        """
        self.ui.apply_button.setEnabled(True)

    @logger.catch
    def changeEvent(self, event):
        """
        处理窗口最小化行为
        :param event: 事件对象
        :return: 无
        """
        if self.windowState() == Qt.WindowState.WindowMinimized:
            logger.debug("设置窗口最小化, 执行隐藏窗口")
            self.showNormal()
            self.setVisible(False)
            self.hide_window_signal.emit()
        else:
            super().changeEvent(event)

    @logger.catch
    def closeEvent(self, event):
        """
        窗口收到关闭事件时隐藏设置窗口
        :param event: 事件对象
        :return: 无
        """
        self.setVisible(False)
        event.ignore()

    @logger.catch
    def load_config(self, configure: dict):
        """
        加载配置
        :param configure: 配置字典
        :return: 无
        """
        QApplication.processEvents()
        self.hide_tray = configure["hide_tray"] or self.default_config["hide_tray"]
        self.forKillExe = configure["forKillExe"] or self.default_config["forKillExe"]
        self.random_time = (
                configure["random_time"] or self.default_config["random_time"]
        )
        self.hold_time = configure["hold_time"] or self.default_config["hold_time"]
        self.forKillWindowTitle = (
                configure["forKillWindowTitle"] or self.default_config["forKillWindowTitle"]
        )

    @logger.catch
    def show_config(self):
        """
        显示配置
        :return: 无
        """
        QApplication.processEvents()
        logger.debug(
            "当前托盘图标透明(0显1透2隐): {}", self.hide_tray, feature="f-strings"
        )
        logger.debug("当前待杀程序: {}", self.forKillExe, feature="f-strings")
        logger.debug("当前随机时间: {}", self.random_time, feature="f-strings")
        logger.debug("当前持续时间: {}", self.hold_time, feature="f-strings")
        logger.debug(
            "当前待杀应用窗口标题: {}", self.forKillWindowTitle, feature="f-strings"
        )

    @logger.catch
    def flash_config(self, configure: dict) -> dict:
        """
        更新配置文件
        :param configure: 配置字典
        :return: 无
        """
        QApplication.processEvents()
        # 将提供的字典对应值设置为当前值
        configure["hide_tray"] = self.hide_tray
        configure["forKillExe"] = self.forKillExe
        configure["random_time"] = self.random_time
        configure["hold_time"] = self.hold_time
        configure["forKillWindowTitle"] = self.forKillWindowTitle
        return configure

    @logger.catch
    def show_window(self):
        """
        显示窗口(获取焦点+活动+前置)
        :return:
        """
        self.setVisible(True)
        self.raise_()
        self.activateWindow()
        self.setFocus()

    @logger.catch
    def change_window_state(self, hide: bool = False):
        """
        显示或隐藏设置窗口
        :param hide:
        :return:
        """
        if hide:
            self.setVisible(False)
        else:
            self.show_window()

    @logger.catch
    def quit_app(self):
        """
        退出软件
        :return: 无
        """
        self.life = False
        keyboard.unhook_all()
        logger.debug(f"当前软件生命状态: {self.life}")
        self.app.quit()
        sys.exit()

    @logger.catch
    def flash_state_changed(self):
        """
        刷新配置
        :return: 无
        """
        QApplication.processEvents()
        # 将当前属性设置为GUI控件的值
        # region 设置待杀程序列表 和 待杀应用程序窗口标题列表
        self.forKillExe = flash_list_widget(self.ui.for_kill_list)
        self.forKillWindowTitle = flash_list_widget(self.ui.for_close_title)
        # endregion
        self.hide_tray = (
            2
            if self.ui.if_strong_hide.isChecked()
            else 1 if self.ui.if_tray_hide.isChecked() else 0
        )
        self.hold_time = self.ui.hold_seconds.value()
        # 判断随机时间范围是否正确(whether a<=b or not)
        if self.ui.a.value() > self.ui.b.value():
            # 不正确,则将两个输入框的值调转
            self.random_time[0] = self.ui.b.value()
            self.random_time[1] = self.ui.a.value()
            self.ui.a.setValue(self.random_time[0])
            self.ui.b.setValue(self.random_time[1])
        else:
            # 如果正确,则将两个输入框的值设置为新的值
            self.random_time[0] = self.ui.a.value()
            self.random_time[1] = self.ui.b.value()
        with open("config.json", "w") as f:
            dump(
                {
                    "hide_tray": self.hide_tray,
                    "forKillExe": self.forKillExe,
                    "random_time": self.random_time,
                    "hold_time": self.hold_time,
                    "forKillWindowTitle": self.forKillWindowTitle,
                },
                f,
                indent=4,
            )
        self.show_config()
        # 将应用按钮设置为禁用状态
        self.ui.apply_button.setDisabled(True)
        # 发送应用信号
        self.apply_signal.emit()

    # endregion
