import sys
import threading
from datetime import datetime, timedelta
from random import randint
from time import sleep

from PySide6.QtWidgets import QSystemTrayIcon, QApplication
from loguru import logger

from public_functions import mapx, kill_exe


class MessageShower:
    """
    自定义消息显示类
    """

    @logger.catch
    def __init__(self, window: "MainWindow", tray_icon: QSystemTrayIcon):
        self.window, self.tray_icon = window, tray_icon
        threading.Thread(target=self.warn).start()

    # region 通知提醒功能实现
    @logger.catch
    def warning_action(self):
        """
        当下课时执行的操作(关闭相关软件!)
        :return:
        """
        now = datetime.now()
        wait_second = (
            randint(self.window.random_time[0], self.window.random_time[1])
            if now.strftime("%H:%M") in self.window.time_config.keys()
               or self.window.test
            else 0
        )
        logger.debug(f"将等待时间: {wait_second}秒")
        while self.window.life and self.window.state:
            if datetime.now() - (now + timedelta(seconds=wait_second)) <= timedelta():
                sleep(1)
                continue
            else:
                logger.debug("关闭窗口中")
                mapx(
                    self.window.window_closer.kill_windows,
                    self.window.forKillWindowTitle,
                )
                logger.debug("杀死进程中")
                mapx(kill_exe, self.window.forKillExe)
                break
        self.window.test = False
        self.window.ui.test_button.setEnabled(True)
        self.window.ui.test_button.setText("测试")

    @logger.catch
    def warn(self):
        """
        警告功能
        :return: 无
        """
        while self.window.life:
            if self.window.state or self.window.test:
                QApplication.processEvents()
                now = datetime.now()
                now = timedelta(
                    hours=now.hour,
                    minutes=now.minute,
                    seconds=now.second,
                )
                for class_over_time in self.window.time_config.keys():
                    hours, minutes = map(int, class_over_time.split(":"))
                    if self.window.test or (
                            timedelta()
                            <= now - timedelta(hours=hours, minutes=minutes)
                            <= timedelta(seconds=self.window.hold_time)
                    ):
                        # 如果差小于持续时间
                        self.window.ui.test_button.setDisabled(True)
                        self.window.ui.test_button.setText("执行中, 请稍候...")
                        logger.debug("执行清剿函数")
                        self.warning_action()
                        break
            sleep(1)
        sys.exit(0)
