from loguru import logger

from classes.basic_classes.EditItem import EditItem


class EditEXE(EditItem):
    """
    自定义编辑待杀程序窗口类
    """

    @logger.catch
    def __init__(self, parent: "MainWindow"):
        super().__init__(parent, parent.ui.for_kill_list)
        self.connect_window.ui.edit_exe_button.clicked.connect(self.edit_item_function)
        self.ui.get_exe_name.returnPressed.connect(self.edit_item_func)
        self.ui.label.setText("重命名待杀程序")
