from os import popen
from pathlib import Path, PurePath
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QListWidget, QWidget, QCheckBox
from loguru import logger

__all__ = [
    "resource_path",
    "set_window_size",
    "kill_exe",
    "flash_list_widget",
    "mapx",
    "connect_signals",
]

@logger.catch
def resource_path(relative_path: str) -> str:
    """
    获取打包后文件资源路径
    :param relative_path: 调试环境路径
    :return: 无
    """
    QApplication.processEvents()
    # noinspection SpellCheckingInspection
    return PurePath.joinpath(Path(__file__).parent, relative_path).__str__()


@logger.catch
def set_window_size(window: QWidget, application: QApplication):
    """
    设置窗口大小位置
    :param application: Qt应用对象
    :param window: 要设置的窗口
    :return:
    """
    # 获取屏幕的尺寸
    available_geometry: QRect = application.screens()[0].availableGeometry()

    # 应用窗口位置
    window.setGeometry(
        available_geometry.width() >> 2,
        available_geometry.height() >> 2,
        available_geometry.width() >> 1,
        available_geometry.height() >> 1,
    )


# noinspection SpellCheckingInspection
@logger.catch
def kill_exe(process: str):
    """
    根据映像名杀死指定进程
    :param process: 进程映像名
    :return:
    """
    if (
        process
        == popen(f'tasklist /nh /fi "IMAGENAME eq {process}"')
        .read()
        .split("\n")[1]
        .split("  ")[0]
    ):
        logger.debug(f"杀死进程{process}")
        popen(f"taskkill /f /im {process}")
    else:
        logger.warning(f"{process}未运行")


@logger.catch
def flash_list_widget(list_widget: QListWidget) -> list:
    """
    排序所传入的列表控件, 并返回所有项的列表
    :param list_widget: 传入的QListWidget对象
    :return:
    """
    if type(list_widget) != QListWidget:
        raise TypeError("list_widget must be QListWidget")
    list_widget.sortItems()
    return [list_widget.item(i).text() for i in range(list_widget.count())]


# noinspection PyShadowingBuiltins
@logger.catch
def mapx(func, iterable: list):
    """
    对可迭代对象中的每个元素应用指定函数, 并返回结果列表
    :param func: 要应用的函数
    :param iterable: 可迭代对象
    :return: 结果列表
    """
    return [func(item) for item in iterable]


@logger.catch
def connect_signals(widgets: list, func) -> list:
    """
    连接QObject对象的信号到指定函数
    :param widgets: QObject对象列表
    :param func: 要连接的函数
    :return: 连接结果列表
    """
    return [
        (
            widget.stateChanged.connect(func)
            if type(widget) == QCheckBox
            else widget.valueChanged.connect(func)
        )
        for widget in widgets
    ]
