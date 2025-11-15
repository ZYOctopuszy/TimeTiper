import pathlib

import keyboard
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QSystemTrayIcon, QApplication, QMenu
from loguru import logger

from public_functions import resource_path


class Tray(QSystemTrayIcon):
    """
    自定义系统托盘图标类
    """

    @logger.catch
    def __init__(self, connect_window: "MainWindow"):
        QApplication.processEvents()
        super().__init__()
        self.files = [
            r"icons\active.png",
            r"icons\inactive.png",
            r"icons\hide_tray.png",
            r"icons\active.ico",
        ]
        self.connect_window = connect_window

        self.setToolTip("那刻夏")

        self.connect_window.apply_signal.connect(self.flash_tray)
        self.connect_window.state_changed_signal.connect(
            lambda: self.change_tray_state(False)
        )
        self.connect_window.hide_window_signal.connect(self.show_hide_window)

        # 创建系统托盘菜单
        self.menu: QMenu = QMenu()

        # "显示"和"隐藏"菜单项
        self.show_hide_action: QAction = QAction("呼叫")
        self.show_hide_action.setToolTip("与那刻夏交谈")
        self.show_hide_action.triggered.connect(lambda: self.show_hide_window(True))
        self.menu.addAction(self.show_hide_action)

        # "启用与禁用"菜单项
        self.enable_disable_action: QAction = QAction("催眠")
        self.enable_disable_action.setToolTip("催眠那刻夏")
        self.enable_disable_action.triggered.connect(self.change_tray_state)
        self.menu.addAction(self.enable_disable_action)

        # "退出"菜单项
        self.exit_action: QAction = QAction("送别")
        self.exit_action.setToolTip("送别那刻夏")
        self.exit_action.triggered.connect(connect_window.quit_app)
        self.menu.addAction(self.exit_action)

        # 应用系统托盘菜单
        self.setContextMenu(self.menu)
        self.set_picture_path()
        self.show()

        # 连接系统托盘图标点击信号与槽函数
        self.activated.connect(self.toggle_window)

    @logger.catch
    def set_picture_path(self):
        """
        设置系统托盘图标图片路径
        :return:
        """
        QApplication.processEvents()
        # 设置图片文件路径
        file_paths = map(resource_path, self.files)

        self.files = [pathlib.Path(i).resolve().__str__() for i in file_paths]
        self.setIcon(QIcon(self.files[0]))
        self.connect_window.setWindowIcon(QIcon(self.files[0]))
        self.connect_window.ui.show_icon.setPixmap(
            QPixmap(self.files[0]).scaled(
                30,
                30,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

    @logger.catch
    def toggle_window(self, reason):
        """
        实现托盘各种点击操作
        :param reason: 点击类型
        :return: 无
        """
        # 托盘双击操作-打开设置
        QApplication.processEvents()
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            if not self.connect_window.isVisible() and (
                    (not self.connect_window.hide_tray) or keyboard.is_pressed("shift+esc")
            ):
                # 显示设置窗口
                logger.debug("显示设置窗口")
                self.show_hide_action.setText("设完了")
                self.show_hide_action.setToolTip("交流完毕")
                self.connect_window.change_window_state()
            elif self.connect_window.isVisible():
                # 隐藏设置窗口
                self.show_hide_action.setText("呼叫")
                self.show_hide_action.setToolTip("与那刻夏交谈")
                self.connect_window.change_window_state(True)

        # 托盘中建操作-关闭软件
        elif reason == QSystemTrayIcon.ActivationReason.MiddleClick:
            self.connect_window.quit_app()

    @logger.catch
    def change_tray_state(self, change_state: bool = True):
        """
        改变托盘图标状态
        :return:
        """
        if change_state:
            self.connect_window.state ^= True
            self.connect_window.ui.is_active.setText(
                "工作中" if self.connect_window.state else "睡觉中"
            )
            logger.debug(f"当前启用状态: {self.connect_window.state}")
        QApplication.processEvents()
        self.enable_disable_action.setText(
            "催眠" if self.connect_window.state else "唤醒"
        )
        if not self.connect_window.hide_tray:
            logger.debug("托盘图标未设置隐藏, 切换托盘图标图片")
            if self.connect_window.state:
                self.setIcon(QIcon(self.files[0]))
                self.setToolTip("那刻夏")
            else:
                self.setIcon(QIcon(self.files[1]))
                self.setToolTip("那刻夏\n(睡觉中)")

    @logger.catch
    def show_hide_window(self, change_window_state: bool = False):
        """
        改变托盘上下文菜单
        :param change_window_state: 是否改变窗口状态
        :return:
        """
        if change_window_state:
            self.connect_window.change_window_state(self.connect_window.isVisible())
        if self.connect_window.isVisible():
            self.show_hide_action.setToolTip("与那刻夏交谈")
            self.show_hide_action.setText("呼叫")
        else:
            self.show_hide_action.setToolTip("交谈完毕")
            self.show_hide_action.setText("设完了")

    @logger.catch
    def flash_tray(self):
        """
        刷新托盘图标状态
        :return:
        """
        self.setVisible(self.connect_window.hide_tray != 2)
        if self.connect_window.hide_tray == 1:
            self.setToolTip("")
            self.setIcon(QIcon(self.files[2]))
        else:
            self.change_tray_state(False)
