from pathlib import PurePath, Path
from sys import stdout, argv, exit

from PySide6.QtWidgets import QApplication
from loguru import logger

from main_classes import *

# 创建日志文件
logger.remove()
logger.add(
    sink=stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <red>|</red> <level>{level}</level> <red>|</red> "
           "<yellow>{name}</yellow> <red>-></red> <yellow>{function}</yellow> <red>-></red> "
           "<yellow>{line}</yellow><red> >>> </red><cyan>{message}</cyan>",
    enqueue=True,
    backtrace=True,
    catch=True,
    colorize=True,
)
logger.add(
    sink=PurePath.joinpath(Path(argv[0]).parent, "TimeTipper.log").__str__(),
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level}</level> | {name} -> {function} -> {line} >>> {message}",
    rotation="1024 MB",
    retention="2days",
    encoding="utf-8",
    compression="zip",
    enqueue=True,
    backtrace=True,
    catch=True,
)


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow(app)
    exit(app.exec())
