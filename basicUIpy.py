from PySide6.QtWidgets import QWidget, QListWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from loguru import logger
from UIs import get_input
class GetInput(QWidget):
    """
    自定义获取输入窗口类
    """

    @logger.catch
    def __init__(self, parent, list_widget: QListWidget):
        super().__init__()
        self.ui = get_input.UiGetInput()
        self.ui.setupUi(self)
        self.window = parent
        self.list_widget = list_widget
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(self.window.tray_icon.files[3]))
        self.hide()


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
            self.window.flash_state_changed()
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
        self.window.flash_state_changed()

    @logger.catch
    def add_item_function(self):
        """
        处理手动添加项
        :return:
        """
        # 显示程序名称输入框
        self.show()
        self.ui.get_exe_name.clear()


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
        self.window.flash_state_changed()