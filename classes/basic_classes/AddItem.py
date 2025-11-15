from PySide6.QtWidgets import QApplication
from loguru import logger

from classes.basic_classes.GetInput import GetInput


class AddItem(GetInput):
    """
    自定义添加项窗口类
    """

    @logger.catch
    def __init__(self, parent, list_widget):
        super().__init__(parent, list_widget)

    @logger.catch
    def remove_item(self):
        """
        删除选中项
        :return:
        """
        QApplication.processEvents()
        try:
            for_remove_item = self.list_widget.currentItem()
            self.list_widget.takeItem(self.list_widget.currentRow())
            logger.debug(f"已删指定项: {for_remove_item.text()}")
            self.connect_window.flash_state_changed()
        except Exception as error:
            logger.warning(f"删除项失败{error}")

    @logger.catch
    def add_item_func(self):
        """
        添加项到列表
        :return:
        """
        QApplication.processEvents()
        self.hide()
        self.list_widget.addItem(self.ui.get_exe_name.text())
        logger.debug(f"已手动添加项: {self.ui.get_exe_name.text()}")
        self.connect_window.flash_state_changed()

    @logger.catch
    def add_item_function(self):
        """
        处理手动添加项
        :return:
        """
        # 显示程序名称输入框
        self.show()
        self.ui.get_exe_name.clear()
