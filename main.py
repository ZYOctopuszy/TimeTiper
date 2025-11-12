from sys import argv

from classes import *


# 创建日志文件
@logger.catch
def set_logger():
    """
    设置日志文件
    :return:
    """

    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <red>|</red> <level>{level}</level> <red>|</red> "
               "<yellow>{name}</yellow> <red>-></red> <yellow>{function}</yellow> <red>-></red> "
               "<yellow>{line}</yellow><red> >>> </red><cyan>{message}</cyan>",
        enqueue=True,
        backtrace=True,
        catch=True,
        colorize=True,
    )
    logger.add(
        sink=path.join(split(abspath(sys.argv[0]))[0], "TimeTipper.log"),
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level}</level> | {name} -> {function} -> {line} >>> {message}",
        rotation="1024 MB",
        retention="2days",
        encoding="utf-8",
        compression="zip",
        enqueue=True,
        backtrace=True,
        catch=True,
    )
set_logger()

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow(app)
    sys.exit(app.exec())
