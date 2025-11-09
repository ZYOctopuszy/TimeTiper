# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QLabel, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(666, 356)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.apply_button = QPushButton(Form)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setEnabled(False)

        self.gridLayout.addWidget(self.apply_button, 1, 2, 1, 1)

        self.exit_button = QPushButton(Form)
        self.exit_button.setObjectName(u"exit_button")

        self.gridLayout.addWidget(self.exit_button, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.times = QWidget()
        self.times.setObjectName(u"times")
        self.gridLayout_2 = QGridLayout(self.times)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.delete_button = QPushButton(self.times)
        self.delete_button.setObjectName(u"delete_button")

        self.gridLayout_2.addWidget(self.delete_button, 4, 2, 1, 1)

        self.description = QTextEdit(self.times)
        self.description.setObjectName(u"description")

        self.gridLayout_2.addWidget(self.description, 1, 1, 5, 1)

        self.add_button = QPushButton(self.times)
        self.add_button.setObjectName(u"add_button")

        self.gridLayout_2.addWidget(self.add_button, 3, 2, 1, 1)

        self.time_list = QListWidget(self.times)
        self.time_list.setObjectName(u"time_list")
        self.time_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.time_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.time_list.setMovement(QListView.Movement.Static)
        self.time_list.setFlow(QListView.Flow.TopToBottom)
        self.time_list.setResizeMode(QListView.ResizeMode.Fixed)
        self.time_list.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.time_list.setViewMode(QListView.ViewMode.ListMode)

        self.gridLayout_2.addWidget(self.time_list, 1, 0, 5, 1)

        self.edit_button = QPushButton(self.times)
        self.edit_button.setObjectName(u"edit_button")

        self.gridLayout_2.addWidget(self.edit_button, 5, 2, 1, 1)

        self.time_tip = QLabel(self.times)
        self.time_tip.setObjectName(u"time_tip")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_tip.sizePolicy().hasHeightForWidth())
        self.time_tip.setSizePolicy(sizePolicy)
        self.time_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.time_tip, 0, 0, 1, 1)

        self.desription_tip = QLabel(self.times)
        self.desription_tip.setObjectName(u"desription_tip")
        sizePolicy.setHeightForWidth(self.desription_tip.sizePolicy().hasHeightForWidth())
        self.desription_tip.setSizePolicy(sizePolicy)
        self.desription_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.desription_tip, 0, 1, 1, 1)

        self.tabWidget.addTab(self.times, "")
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.gridLayout_5 = QGridLayout(self.settings)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.is_active = QPushButton(self.settings)
        self.is_active.setObjectName(u"is_active")

        self.gridLayout_5.addWidget(self.is_active, 0, 2, 1, 1)

        self.frame = QFrame(self.settings)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.if_tray_hide = QCheckBox(self.frame)
        self.if_tray_hide.setObjectName(u"if_tray_hide")

        self.gridLayout_7.addWidget(self.if_tray_hide, 0, 0, 1, 4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.label_4, 2, 2, 1, 1)

        self.a = QSpinBox(self.frame)
        self.a.setObjectName(u"a")
        self.a.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.a, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 4, 0, 1, 4)

        self.b = QSpinBox(self.frame)
        self.b.setObjectName(u"b")
        self.b.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.b, 2, 3, 1, 1)

        self.hold_seconds = QSpinBox(self.frame)
        self.hold_seconds.setObjectName(u"hold_seconds")
        self.hold_seconds.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.hold_seconds, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)

        self.if_strong_hide = QCheckBox(self.frame)
        self.if_strong_hide.setObjectName(u"if_strong_hide")

        self.gridLayout_7.addWidget(self.if_strong_hide, 1, 0, 1, 4)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 3, 1)

        self.test_button = QPushButton(self.settings)
        self.test_button.setObjectName(u"test_button")

        self.gridLayout_5.addWidget(self.test_button, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 3, 1)

        self.tabWidget.addTab(self.settings, "")
        self.executables = QWidget()
        self.executables.setObjectName(u"executables")
        self.gridLayout_6 = QGridLayout(self.executables)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.executables)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.exe = QWidget()
        self.exe.setObjectName(u"exe")
        self.gridLayout_8 = QGridLayout(self.exe)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.edit_exe_button = QPushButton(self.exe)
        self.edit_exe_button.setObjectName(u"edit_exe_button")

        self.gridLayout_8.addWidget(self.edit_exe_button, 2, 1, 1, 1)

        self.remove_exe = QPushButton(self.exe)
        self.remove_exe.setObjectName(u"remove_exe")

        self.gridLayout_8.addWidget(self.remove_exe, 4, 1, 1, 1)

        self.add_exe = QPushButton(self.exe)
        self.add_exe.setObjectName(u"add_exe")

        self.gridLayout_8.addWidget(self.add_exe, 3, 1, 1, 1)

        self.choose_exe = QPushButton(self.exe)
        self.choose_exe.setObjectName(u"choose_exe")

        self.gridLayout_8.addWidget(self.choose_exe, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.for_kill_list = QListWidget(self.exe)
        self.for_kill_list.setObjectName(u"for_kill_list")

        self.gridLayout_8.addWidget(self.for_kill_list, 0, 0, 5, 1)

        self.tabWidget_2.addTab(self.exe, "")
        self.title = QWidget()
        self.title.setObjectName(u"title")
        self.gridLayout_9 = QGridLayout(self.title)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.remove_title = QPushButton(self.title)
        self.remove_title.setObjectName(u"remove_title")

        self.gridLayout_9.addWidget(self.remove_title, 3, 1, 1, 1)

        self.add_title = QPushButton(self.title)
        self.add_title.setObjectName(u"add_title")

        self.gridLayout_9.addWidget(self.add_title, 2, 1, 1, 1)

        self.edit_title_button = QPushButton(self.title)
        self.edit_title_button.setObjectName(u"edit_title_button")

        self.gridLayout_9.addWidget(self.edit_title_button, 1, 1, 1, 1)

        self.for_close_title = QListWidget(self.title)
        self.for_close_title.setObjectName(u"for_close_title")

        self.gridLayout_9.addWidget(self.for_close_title, 0, 0, 4, 1)

        self.tabWidget_2.addTab(self.title, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 2, 1, 1, 1)

        self.tabWidget.addTab(self.executables, "")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.gridLayout_4 = QGridLayout(self.about)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.about)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(69)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.about)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.about, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)

        QWidget.setTabOrder(self.tabWidget, self.time_list)
        QWidget.setTabOrder(self.time_list, self.add_button)
        QWidget.setTabOrder(self.add_button, self.delete_button)
        QWidget.setTabOrder(self.delete_button, self.edit_button)
        QWidget.setTabOrder(self.edit_button, self.exit_button)
        QWidget.setTabOrder(self.exit_button, self.apply_button)
        QWidget.setTabOrder(self.apply_button, self.if_tray_hide)
        QWidget.setTabOrder(self.if_tray_hide, self.if_strong_hide)
        QWidget.setTabOrder(self.if_strong_hide, self.a)
        QWidget.setTabOrder(self.a, self.b)
        QWidget.setTabOrder(self.b, self.hold_seconds)
        QWidget.setTabOrder(self.hold_seconds, self.is_active)
        QWidget.setTabOrder(self.is_active, self.test_button)
        QWidget.setTabOrder(self.test_button, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.for_kill_list)
        QWidget.setTabOrder(self.for_kill_list, self.choose_exe)
        QWidget.setTabOrder(self.choose_exe, self.edit_exe_button)
        QWidget.setTabOrder(self.edit_exe_button, self.add_exe)
        QWidget.setTabOrder(self.add_exe, self.remove_exe)
        QWidget.setTabOrder(self.remove_exe, self.for_close_title)
        QWidget.setTabOrder(self.for_close_title, self.edit_title_button)
        QWidget.setTabOrder(self.edit_title_button, self.add_title)
        QWidget.setTabOrder(self.add_title, self.remove_title)
        QWidget.setTabOrder(self.remove_title, self.description)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TimeTiper", None))
#if QT_CONFIG(tooltip)
        self.apply_button.setToolTip(QCoreApplication.translate("Form", u"\u4e00\u4e9b\u8bbe\u7f6e\u66f4\u6539\u540e\u8981\u5e94\u7528\u624d\u4f1a\u4fdd\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.apply_button.setText(QCoreApplication.translate("Form", u"\u5e94\u7528(Alt+A)", None))
        self.exit_button.setText(QCoreApplication.translate("Form", u"\u9000\u51fa(Ctrl+Q)", None))
#if QT_CONFIG(accessibility)
        self.times.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.delete_button.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.edit_button.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
        self.time_tip.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.desription_tip.setText(QCoreApplication.translate("Form", u"\u63cf\u8ff0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.times), QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.is_active.setToolTip(QCoreApplication.translate("Form", u"\u70b9\u51fb\u5207\u6362\u6fc0\u6d3b\u72b6\u6001", None))
#endif // QT_CONFIG(tooltip)
        self.is_active.setText(QCoreApplication.translate("Form", u"\u5de5\u4f5c\u4e2d", None))
#if QT_CONFIG(tooltip)
        self.if_tray_hide.setToolTip(QCoreApplication.translate("Form", u"\u5c06\u6258\u76d8\u56fe\u6807\u8bbe\u7f6e\u4e3a\u900f\u660e\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.if_tray_hide.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u6258\u76d8", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"\u4e0b\u8bfe\u540e\u591a\u957f\u65f6\u95f4\u5185\u4e0d\u53ef\u4ee5\u518d\u6b21\u6253\u5f00\u6559\u5b66\u8f6f\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6301\u7eed\u65f6\u95f4(\u79d2)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"~", None))
#if QT_CONFIG(tooltip)
        self.a.setToolTip(QCoreApplication.translate("Form", u"\u5ef6\u8fdf\u6700\u5c0f\u503c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.b.setToolTip(QCoreApplication.translate("Form", u"\u5ef6\u8fdf\u6700\u5927\u503c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"\u5f53\u4e0b\u8bfe\u540e\u4f1a\u968f\u673a\u5728\u8fd9\u4e2a\u8303\u56f4\u5185\u53d6\u503c\u4f5c\u4e3a\u5ef6\u8fdf, \u7136\u540e\u7b49\u5f85\u5ef6\u8fdf\u540e\u518d\u6740\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"\u968f\u673a\u7b49\u5f85\u65f6\u95f4(\u79d2)", None))
        self.if_strong_hide.setText(QCoreApplication.translate("Form", u"\u5f3a\u529b\u9690\u85cf\u6a21\u5f0f(\u8bf7\u4f7f\u7528ctrl+win+alt+shift+f6\u6253\u5f00\u8bbe\u7f6e, \u6258\u76d8\u56fe\u6807\u5c06\u6d88\u5931)", None))
#if QT_CONFIG(tooltip)
        self.test_button.setToolTip(QCoreApplication.translate("Form", u"\u6a21\u62df\u4e00\u6b21\u4e0b\u8bfe", None))
#endif // QT_CONFIG(tooltip)
        self.test_button.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.edit_exe_button.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.remove_exe.setText(QCoreApplication.translate("Form", u"-", None))
        self.add_exe.setText(QCoreApplication.translate("Form", u"+", None))
        self.choose_exe.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.exe), QCoreApplication.translate("Form", u"\u5e94\u7528\u7a0b\u5e8fexe", None))
        self.remove_title.setText(QCoreApplication.translate("Form", u"-", None))
        self.add_title.setText(QCoreApplication.translate("Form", u"+", None))
        self.edit_title_button.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.title), QCoreApplication.translate("Form", u"\u7a97\u53e3\u6807\u9898", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.executables), QCoreApplication.translate("Form", u"\u7a0b\u5e8f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u90a3\u523b\u590f\uff01", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e00\u4f4d\u95f2\u7740\u6ca1\u4e8b\u7684\u521d\u4e09\u751f\u5199\u7684\u5c0f\u7a0b\u5e8f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
    # retranslateUi

