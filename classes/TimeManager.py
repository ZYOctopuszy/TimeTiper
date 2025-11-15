from json import dump

from PySide6.QtCore import QTime
from PySide6.QtWidgets import QApplication, QListWidgetItem
from loguru import logger

import classes


class TimeManager:
    """
    管理时间列表
    """

    def __init__(self, window: "MainWindow"):
        self.window = window
        self.add_time = classes.AddTime('add_time')
        self.edit_time = classes.AddTime('edit_time')

        self.window.ui.add_button.clicked.connect(
            lambda: self.add_time.show() and self.add_time.ui.timeEdit.clear()
        )
        self.window.ui.edit_button.clicked.connect(self.edit_button_action)
        self.window.ui.delete_button.clicked.connect(self.delete_button_action)

        self.add_time.ui.sure.clicked.connect(self.add_button_action)
        self.edit_time.ui.sure.clicked.connect(self.edit_time_function)

    # region 时间编辑功能函数
    @logger.catch
    def add_button_action(self):
        """
        添加提醒时间
        :return: 无
        """
        QApplication.processEvents()
        self.add_time.hide()
        # 格式化时间字符串为"小时:分钟"格式
        if (
                added_time := self.add_time.ui.timeEdit.time().toString("HH:mm")
        ) not in self.window.time_config.keys():
            self.window.time_config[added_time] = "Default Description"
            self.window.ui.time_list.clear()
            self.window.ui.time_list.addItems(sorted(self.window.time_config.keys()))
            self.edit_description()

    @logger.catch
    def delete_button_action(self):
        """
        删除当前选中项
        :return: 无
        """
        QApplication.processEvents()
        if current_item := self.window.ui.time_list.currentItem():
            self.window.ui.time_list.takeItem(
                self.window.ui.time_list.currentRow())
            del self.window.time_config[current_item.text()]
            self.flash_time_config()

    @logger.catch
    def edit_button_action(self):
        """
        显示时间编辑框
        :return:
        """
        QApplication.processEvents()
        if (
                type(current_item := self.window.ui.time_list.currentItem())
                is QListWidgetItem
        ):
            self.edit_time.ui.timeEdit.setTime(
                QTime.fromString(current_item.text(), "HH:mm")
            )
            self.edit_time.show()

    @logger.catch
    def edit_time_function(self):
        """
        编辑选中时间项
        :return:
        """
        self.edit_time.hide()
        before_time: str = self.window.ui.time_list.currentItem().text()
        if (
                new_time := self.edit_time.ui.timeEdit.time().toString("HH:mm")
        ) not in self.window.time_config.keys():
            self.window.ui.time_list.currentItem().setText(new_time)
            self.window.time_config[new_time] = self.window.time_config.pop(
                before_time, None
            )
            self.window.ui.time_list.sortItems()
            self.flash_time_config()

    # endregion

    # region 时间描述操作相关
    @logger.catch
    def flash_description(self):
        """
        展示当前选中项的描述
        :return: 无
        """
        QApplication.processEvents()
        if current_item := self.window.ui.time_list.currentItem():
            logger.debug(f"当前选中: {current_item.text()}")
            self.window.ui.description.setText(
                self.window.time_config[current_item.text()]
            )

    @logger.catch
    def edit_description(self):
        """
        刷新当前选中项的描述
        :return: 无
        """
        QApplication.processEvents()

        if current_item := self.window.ui.time_list.currentItem():
            self.window.time_config[current_item.text()] = (
                self.window.ui.description.toPlainText()
            )
            self.flash_time_config()

    @logger.catch
    def flash_time_config(self):
        """
        刷新时间表配置
        :return:
        """
        self.window.time_config = {k: self.window.time_config[k] for k in sorted(self.window.time_config.keys())}
        logger.debug(f"已刷新时间表配置, 当前配置:{self.window.time_config}")
        with open("clock.json", "w", encoding="utf-8") as f:
            dump(self.window.time_config, f, ensure_ascii=False, indent=4)

    # endregion
