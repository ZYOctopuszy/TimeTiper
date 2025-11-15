from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from loguru import logger

from classes.basic_classes.MyQWidget import MyQWidget

from UIs import get_input
from PySide6.QtWidgets import QListWidget


class GetInput(MyQWidget):
    """
    自定义获取输入窗口类
    """

    @logger.catch
    def __init__(self, parent: "MainWindow", list_widget: QListWidget):
        super().__init__()
        self.ui = get_input.Ui_get_input()
        self.ui.setupUi(self)
        self.connect_window = parent
        self.list_widget = list_widget
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(self.connect_window.tray_icon.files[3]))
        self.hide()
