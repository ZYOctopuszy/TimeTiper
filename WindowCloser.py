import win32con, win32gui
from loguru import logger


class WindowCloser:
    """
    窗口关闭类
    """

    def __init__(self):
        self.hwnd_list = []

    def kill_windows(self, title: str = ""):
        """
        关闭所有匹配标题的窗口
        :param title: 窗口标题
        """
        win32gui.EnumWindows(self.callback, title)
        [win32gui.PostMessage(hwnd, win32con.WM_CLOSE) for hwnd in self.hwnd_list]
        self.hwnd_list.clear()

    def callback(self, hwnd, extra):
        """
        枚举窗口回调函数，用于查找匹配标题的窗口
        :param hwnd: 窗口句柄
        :param extra: 窗口标题包含的字符串
        """
        window_title = win32gui.GetWindowText(hwnd)
        if (
            extra.lower() in window_title.lower()
            and win32gui.IsWindowVisible(hwnd)
            and win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
        ):
            logger.debug(f"找到匹配窗口 - 句柄: {hwnd}, 标题: {window_title}")
            self.hwnd_list.append(hwnd)
            # 如果只需要第一个匹配项，可以在这里返回hwnd并停止枚举


if __name__ == "__main__":
    WindowCloser().kill_windows("cmd")
