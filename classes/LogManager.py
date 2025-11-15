from PySide6.QtCore import QObject, Signal
from loguru import logger


class LogManager(QObject):
    update_log = Signal(str)

    @logger.catch
    def __init__(self, window: "MainWindow"):
        super().__init__()
        self.window = window
        # self.window.ui.logger.setLineWrapMode(QTextBrowser.LineWrapMode.NoWrap)
        self.update_log.connect(self.window.ui.logger.append)
        logger.add(
            sink=self,
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name} -> {function} -> {line} >>> {message}",
            enqueue=True,
            backtrace=True,
            catch=True,
        )
        self.gun = self.become_colorful(text=" | ")
        self.curser = self.become_colorful(text=" -> ")
        self.three_cursers = self.become_colorful(text=" >>> ")

    @logger.catch
    def write(self, message: str):
        """
        写入日志
        :param message: 日志内容
        :return:
        """
        message_list = message.splitlines()
        txt_l = message_list[0].split(" | ")
        txt_l = txt_l[:-1] + txt_l[-1].split(" -> ")
        txt_l = txt_l[:-1] + txt_l[-1].split(" >>> ")

        context = (
                self.become_colorful(text=txt_l[0], color="green") + self.gun  # 时间
                + self.become_colorful(text=txt_l[1], color="blue"
        if txt_l[1] == "DEBUG" else "yellow"
        if txt_l[1] == "WARNING" else "red") + self.gun  # 日志等级
                + self.become_colorful(text=txt_l[2], color="orange") + self.curser  # 文件名
                + self.become_colorful(text=txt_l[3], color="orange") + self.curser  # 函数名
                + self.become_colorful(text=txt_l[4], color="orange") + self.three_cursers  # 行号
                + self.become_colorful(text=txt_l[5], color="cyan")
        )

        if len(message_list) > 1:
            for line in message_list[1:]:
                context += "\n<br>" + self.become_colorful(
                    text=line.replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&nbsp;"))

        self.update_log.emit(context)

    @logger.catch
    def become_colorful(self, text: str, color: str = 'red') -> str:
        """
        将文本转换为指定颜色的字体
        :param text: 要转换的文本
        :param color: 字体颜色
        :return: 转换后的文本
        """
        return f"<font color='{color}' face='Cascadia Mono', 'Cascadia Code', 'Microsoft YaHei'>{text}</font>"
