from loguru import logger

from classes.basic_classes.EditItem import EditItem


class EditTitle(EditItem):
    """
    自定义编辑待关闭窗口标题窗口类
    """

    @logger.catch
    def __init__(self, parent: "MainWindow"):
        super().__init__(parent, parent.ui.for_close_title)
        self.ui.label.setText("重命名待关闭窗口标题")
        self.ui.get_exe_name.setPlaceholderText("请输入待杀窗口标题")
        self.connect_window.ui.edit_title_button.clicked.connect(self.edit_item_function)
