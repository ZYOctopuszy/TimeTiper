import os.path, sys
from os import popen
from os.path import join, abspath

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QListWidget, QWidget, QCheckBox, QSpinBox
from loguru import logger


def resource_path(relative_path: str) -> str:
    """
    获取打包后文件资源路径
    :param relative_path: 调试环境路径
    :return: 无
    """
    QApplication.processEvents()
    # noinspection SpellCheckingInspection
    return join(os.path.dirname(__file__), relative_path)


def set_window_size(window: QWidget, application: QApplication):
    """
    设置窗口大小位置
    :param application: Qt应用对象
    :param window: 要设置的窗口
    :return:
    """
    # 获取屏幕的尺寸
    available_geometry: QRect = application.screens()[0].availableGeometry()

    # 计算窗口的位置和尺寸，使窗口居中显示
    window_width: int = available_geometry.width() // 2
    window_height: int = available_geometry.height() // 2
    window_x: int = (
        available_geometry.x() + (available_geometry.width() - window_width) // 2
    )
    window_y: int = (
        available_geometry.y() + (available_geometry.height() - window_height) // 2
    )

    # 应用窗口位置
    window.setGeometry(window_x, window_y, window_width, window_height)


# noinspection SpellCheckingInspection
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
        logger.debug(f"正在杀死进程{process}")
        popen(f"taskkill /f /im {process}")
        logger.debug(f"已杀死进程: {process}")
    else:
        logger.debug(f"{process}未运行")


def flash_list_widget(list_widget: QListWidget) -> list:
    """
    排序所传入的列表控件, 并返回所有项的列表
    :param list_widget: 传入的QListWidget对象
    :return:
    """
    if type(list_widget) == QListWidget:
        list_widget.sortItems()
        return [list_widget.item(i).text() for i in range(list_widget.count())]
    return []


# noinspection PyShadowingBuiltins
def map(func, iterable: list):
    """
    对可迭代对象中的每个元素应用指定函数, 并返回结果列表
    :param func: 要应用的函数
    :param iterable: 可迭代对象
    :return: 结果列表
    """
    return [func(item) for item in iterable]


def connect_signals(widgets: list, func):
    """
    连接QObject对象的信号到指定函数
    :param widgets: QObject对象列表
    :param func: 要连接的函数
    :return:
    """
    return [
        (
            widget.stateChanged.connect(func)
            if type(widget) == QCheckBox
            else widget.valueChanged.connect(func)
        )
        for widget in widgets
    ]
