import keyboard
from PySide6.QtCore import QObject, Signal
from loguru import logger


class HotKeyManager(QObject):
    """
    热键管理类
    """
    show_window_signal = Signal()

    @logger.catch
    def __init__(self, parent: "MainWindow"):
        super().__init__()
        self.window = parent
        keyboard.add_hotkey("ctrl+windows+alt+shift+f6", self.show_window)

    @logger.catch
    def show_window(self):
        """
        显示设置窗口
        :return:
        """
        if self.window.hide_tray == 2:
            self.show_window_signal.emit()
