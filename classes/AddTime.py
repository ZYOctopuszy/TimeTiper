from PySide6.QtCore import Qt
from loguru import logger

from UIs import add_time
from classes import *

class AddTime(basic_classes.MyQWidget.MyQWidget):
    """
    自定义添加时间点窗口类
    """

    @logger.catch
    def __init__(self, use_to: str):
        """
        初始化添加时间点窗口
        :param use_to: 窗口用途, 用于设置窗口标题, 必须为"add_time"或"edit_time"
        """
        super().__init__()
        self.ui = add_time.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        (
            self.setWindowTitle("添加时间点")
            if use_to == "add_time"
            else (
                self.setWindowTitle("编辑时间点")
                if use_to == "edit_time"
                else exec(
                    "raise ValueError('use_to must be 'add_time' or 'edit_time'')"
                )
            )
        )
        self.hide()
