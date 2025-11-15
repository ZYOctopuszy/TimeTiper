import pathlib

from PySide6.QtWidgets import QApplication, QFileDialog
from loguru import logger

from classes.basic_classes.AddItem import AddItem
from public_functions import kill_exe


class AddEXE(AddItem):
    """
    自定义添加待杀程序窗口类
    """

    @logger.catch
    def __init__(self, parent: "MainWindow"):
        super().__init__(parent, parent.ui.for_kill_list)
        self.connect_window.ui.remove_exe.clicked.connect(self.remove_item)
        self.connect_window.ui.add_exe.clicked.connect(self.add_item_function)
        self.connect_window.ui.choose_exe.clicked.connect(self.add_exe_by_choose_file)
        self.ui.get_exe_name.returnPressed.connect(self.add_item_func)
        self.connect_window.ui.for_kill_list.itemDoubleClicked.connect(
            self.item_double_clicked_action
        )
        self.ui.label.setText("添加待杀程序")

    @logger.catch
    def add_exe_by_choose_file(self):
        """
        通过选择文件添加待杀程序
        :return: 无
        """
        file_name = pathlib.Path(
            QFileDialog.getOpenFileName(self.connect_window, "选择待杀程序", "", "*.exe")[0]
        ).name
        if file_name.strip() != "":
            self.connect_window.ui.for_kill_list.addItem(file_name)
            logger.debug(f"已添加待杀程序: {file_name}")
        self.connect_window.flash_state_changed()

    @logger.catch
    def item_double_clicked_action(self):
        """
        双击待杀程序列表项时执行
        :return:
        """
        QApplication.processEvents()
        kill_exe(self.connect_window.ui.for_kill_list.currentItem().text())
