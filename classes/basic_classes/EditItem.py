from PySide6.QtWidgets import QApplication
from loguru import logger

from classes.basic_classes.GetInput import GetInput



class EditItem(GetInput):
    """
    自定义编辑项窗口类
    """

    @logger.catch
    def __init__(self, parent, list_widget):
        super().__init__(parent, list_widget)

    @logger.catch
    def edit_item_function(self):
        """
        处理编辑项
        :return:
        """
        QApplication.processEvents()
        if self.list_widget.currentItem() is not None:
            self.show()
            self.ui.get_exe_name.setText(self.list_widget.currentItem().text())

    @logger.catch
    def edit_item_func(self):
        """
        处理编辑项函数
        :return:
        """
        QApplication.processEvents()
        self.hide()
        current_item = self.list_widget.currentItem()
        self.list_widget.takeItem(self.list_widget.currentRow())
        self.list_widget.addItem(self.ui.get_exe_name.text())
        logger.debug(
            f"已修改项: {current_item.text()} -> {self.ui.get_exe_name.text()}"
        )
        self.connect_window.flash_state_changed()
