from sys import argv
from classes import *

# 创建日志文件
log_file_path = os.path.join(os.path.dirname(sys.executable), "TimeTipper.log") if hasattr(sys, "_MEIPASS") else "TimeTipper.log"
logger.debug(f"日志文件路径: {os.path.abspath(log_file_path)}")
logger.add(
    sink=log_file_path,
    rotation="1024 MB",
    retention="2days",
    encoding="utf-8",
)

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow(app)
    window.setWindowTitle("那刻夏")
    set_window_size(window, app)
    window.thread.start()
    sys.exit(app.exec())
