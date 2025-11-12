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
        Form.resize(601, 310)
        Form.setStyleSheet(u"/* \u57fa\u7840\u8bbe\u7f6e */\n"
"* {\n"
"    font-family: 'Microsoft YaHei', 'Segoe UI', sans-serif;\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"/* \u4e3b\u7a97\u53e3 */\n"
"QWidget#Form {\n"
"    background-color: rgba(20, 30, 20, 0.95);\n"
"    border: 1px solid rgba(60, 90, 60, 0.7);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u9875\u5bb9\u5668 */\n"
"QTabWidget::pane {\n"
"    border: 1px solid rgba(50, 80, 50, 0.8);\n"
"    background: rgba(30, 50, 30, 0.85);\n"
"    border-radius: 6px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u9875\u6807\u7b7e */\n"
"QTabBar::tab {\n"
"    background: rgba(40, 60, 40, 0.8);\n"
"    border: 1px solid rgba(70, 100, 70, 0.6);\n"
"    border-bottom: none;\n"
"    color: #b0d0b0;\n"
"    padding: 6px 12px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgba(60, 90, 60, 0.9);\n"
"    color: white;\n"
"    border-bottom: 1px solid rgba(60, 90,"
                        " 60, 0.9);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: rgba(80, 110, 80, 0.8);\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u6309\u94ae\u57fa\u7840\u6837\u5f0f */\n"
"QPushButton {\n"
"    background-color: rgba(50, 120, 60, 0.85);\n"
"    color: white;\n"
"    border: 1px solid rgba(80, 150, 90, 0.7);\n"
"    border-radius: 4px;\n"
"    padding: 6px 12px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(70, 140, 80, 0.9);\n"
"    border-color: rgba(100, 170, 110, 0.8);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(30, 100, 40, 0.9);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgba(50, 60, 50, 0.7);\n"
"    color: rgba(150, 170, 150, 0.7);\n"
"    border-color: rgba(70, 80, 70, 0.6);\n"
"}\n"
"\n"
"/* \u7279\u6b8a\u6309\u94ae\u6837\u5f0f */\n"
"QPushButton#is_active {\n"
"    background-color: rgba(80, 160, 90, 0.85);\n"
"    border-color: rgba(110, 190, 120, 0.7);\n"
"}\n"
"\n"
"QPushButton#is_active:hover {\n"
"    ba"
                        "ckground-color: rgba(100, 180, 110, 0.9);\n"
"}\n"
"\n"
"QPushButton#test_button {\n"
"    background-color: rgba(120, 60, 50, 0.85);\n"
"    border-color: rgba(150, 90, 80, 0.7);\n"
"}\n"
"\n"
"QPushButton#test_button:hover {\n"
"    background-color: rgba(140, 80, 70, 0.9);\n"
"}\n"
"\n"
"/* \u5217\u8868\u548c\u6587\u672c\u7f16\u8f91\u6846 */\n"
"QListWidget, QTextEdit {\n"
"    background-color: rgba(40, 50, 40, 0.8);\n"
"    border: 1px solid rgba(70, 90, 70, 0.7);\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #e0e0e0;\n"
"    selection-background-color: rgba(60, 120, 70, 0.7);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* \u590d\u9009\u6846 */\n"
"QCheckBox {\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid rgba(90, 120, 90, 0.7);\n"
"    border-radius: 3px;\n"
"    background: rgba(50, 60, 50, 0.8);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
""
                        "    background: rgba(60, 130, 70, 0.9);\n"
"    image: url(:/icons/checkmark.png);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    background-color: rgba(70, 80, 70, 0.3);\n"
"}\n"
"\n"
"/* \u6570\u503c\u8f93\u5165\u6846 */\n"
"QSpinBox {\n"
"    background-color: rgba(40, 50, 40, 0.8);\n"
"    border: 1px solid rgba(70, 90, 70, 0.7);\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 16px;\n"
"    border: none;\n"
"    background: rgba(60, 80, 60, 0.7);\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background: rgba(80, 100, 80, 0.8);\n"
"}\n"
"\n"
"/* \u6846\u67b6\u6837\u5f0f */\n"
"QFrame {\n"
"    background-color: rgba(35, 45, 35, 0.8);\n"
"    border: 1px solid rgba(70, 90, 70, 0.6);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* \u6807\u7b7e\u6837\u5f0f */\n"
"QLabel {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u5173\u4e8e\u9875\u5927\u6807\u9898 */\n"
"QLabel#label {\n"
" "
                        "   color: rgba(100, 220, 120, 0.9);\n"
"    text-shadow: 1px 1px 2px rgba(0, 10, 0, 0.3);\n"
"}\n"
"\n"
"/* \u5206\u9694\u7ebf */\n"
"QFrame[frameShape=\"4\"], QFrame[frameShape=\"5\"] {\n"
"    background-color: rgba(70, 90, 70, 0.6);\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761 */\n"
"QScrollBar:vertical {\n"
"    background: rgba(40, 50, 40, 0.5);\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(80, 120, 80, 0.6);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u5de5\u5177\u63d0\u793a */\n"
"QToolTip {\n"
"    background-color: rgba(40, 50, 40, 0.95);\n"
"    color: #e0e0e0;\n"
"    border: 1px solid rgba(70, 100, 70, 0.8);\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"/* \u6dfb\u52a0\u6309\u94ae(+) */\n"
"QPushButton[text=\"+\"], \n"
"QPushButton[text=\"\u6dfb\u52a0\"] {\n"
"    background-color: rgba(70, 1"
                        "50, 80, 0.9);\n"
"}\n"
"\n"
"/* \u5220\u9664\u6309\u94ae(-) */\n"
"QPushButton[text=\"-\"], \n"
"QPushButton[text=\"\u5220\u9664\"] {\n"
"    background-color: rgba(150, 70, 60, 0.9);\n"
"}\n"
"\n"
"/* \u5e94\u7528\u6309\u94ae\u7279\u6b8a\u6837\u5f0f */\n"
"QPushButton[text=\"\u5e94\u7528(Alt+A)\"] {\n"
"    background-color: rgba(80, 140, 90, 0.9);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \u9000\u51fa\u6309\u94ae\u7279\u6b8a\u6837\u5f0f */\n"
"QPushButton[text=\"\u9000\u51fa(Ctrl+Q)\"] {\n"
"    background-color: rgba(120, 60, 50, 0.85);\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.apply_button = QPushButton(Form)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setEnabled(False)

        self.gridLayout.addWidget(self.apply_button, 2, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.exit_button = QPushButton(Form)
        self.exit_button.setObjectName(u"exit_button")

        self.gridLayout.addWidget(self.exit_button, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

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
        self.edit_button.setStyleSheet(u"")

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 3, 0, 1, 1)

        self.if_tray_hide = QCheckBox(self.frame)
        self.if_tray_hide.setObjectName(u"if_tray_hide")

        self.gridLayout_7.addWidget(self.if_tray_hide, 0, 0, 1, 4)

        self.b = QSpinBox(self.frame)
        self.b.setObjectName(u"b")
        self.b.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.b, 2, 3, 1, 1)

        self.if_strong_hide = QCheckBox(self.frame)
        self.if_strong_hide.setObjectName(u"if_strong_hide")

        self.gridLayout_7.addWidget(self.if_strong_hide, 1, 0, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 4, 0, 1, 4)

        self.hold_seconds = QSpinBox(self.frame)
        self.hold_seconds.setObjectName(u"hold_seconds")
        self.hold_seconds.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.hold_seconds, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.label_4, 2, 2, 1, 1)

        self.a = QSpinBox(self.frame)
        self.a.setObjectName(u"a")
        self.a.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.a, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 3, 1)

        self.test_button = QPushButton(self.settings)
        self.test_button.setObjectName(u"test_button")

        self.gridLayout_5.addWidget(self.test_button, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 1, 3, 1)

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

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.minimize_button = QPushButton(self.widget)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setStyleSheet(u"/* \u6700\u5c0f\u5316\u6309\u94ae\u6837\u5f0f - \u6697\u8272\u4e3b\u9898\u4e0e\u7eff\u8272\u8c03\u534f\u8c03 */\n"
"QPushButton#minimize_button {\n"
"    background-color: rgba(50, 60, 50, 0.85);  /* \u6df1\u7eff\u8272\u8c03\u80cc\u666f */\n"
"    border: 1px solid rgba(80, 100, 80, 0.7);  /* \u6d45\u7eff\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"-\";  /* \u4f7f\u7528\u4e0b\u5212\u7ebf\u4f5c\u4e3a\u6700\u5c0f\u5316\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7eff\u8272\u8c03 */\n"
"QPushButton#minimize_button:hover {\n"
"    background-color: rgba(70, 90, 70, 0.9);\n"
"    border-color: rgba(100, 130, 100, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#minimize_button:pressed {\n"
"    background-color: rgba(90, 110, 90, 0.9);\n"
"    border-color: rgba(12"
                        "0, 150, 120, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#minimize_button:disabled {\n"
"    background-color: rgba(50, 60, 50, 0.6);\n"
"    border-color: rgba(70, 80, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_10.addWidget(self.minimize_button, 2, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.close_button = QPushButton(self.widget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setStyleSheet(u"QPushButton#close_button {\n"
"    background-color: rgba(80, 40, 40, 0.85);  /* \u6df1\u7ea2\u8910\u8272\u80cc\u666f */\n"
"    border: 1px solid rgba(120, 60, 60, 0.7);  /* \u7ea2\u8910\u8272\u8fb9\u6846 */\n"
"    border-radius: 4px;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    min-width: 20px;\n"
"    max-width: 20px;\n"
"    min-height: 20px;\n"
"    max-height: 20px;\n"
"    font-weight: bold;\n"
"    qproperty-text: \"\u00d7\";  /* \u4f7f\u7528\u4e58\u53f7\u4f5c\u4e3a\u5173\u95ed\u7b26\u53f7 */\n"
"}\n"
"\n"
"/* \u60ac\u505c\u72b6\u6001 - \u589e\u5f3a\u7ea2\u8272\u8c03\u4f46\u4ecd\u4fdd\u6301\u534f\u8c03 */\n"
"QPushButton#close_button:hover {\n"
"    background-color: rgba(120, 60, 60, 0.9);\n"
"    border-color: rgba(150, 80, 80, 0.8);\n"
"}\n"
"\n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QPushButton#close_button:pressed {\n"
"    background-color: rgba(150, 70, 70, 0.9);\n"
"    border-color: rgba(180, 90, 90, 0.8);\n"
"}\n"
"\n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QPushButton#close_button:disab"
                        "led {\n"
"    background-color: rgba(60, 50, 50, 0.6);\n"
"    border-color: rgba(80, 70, 70, 0.5);\n"
"    color: rgba(180, 180, 180, 0.5);\n"
"}")

        self.gridLayout_10.addWidget(self.close_button, 2, 2, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        QWidget.setTabOrder(self.tabWidget, self.time_list)
        QWidget.setTabOrder(self.time_list, self.add_button)
        QWidget.setTabOrder(self.add_button, self.delete_button)
        QWidget.setTabOrder(self.delete_button, self.edit_button)
        QWidget.setTabOrder(self.edit_button, self.if_tray_hide)
        QWidget.setTabOrder(self.if_tray_hide, self.if_strong_hide)
        QWidget.setTabOrder(self.if_strong_hide, self.a)
        QWidget.setTabOrder(self.a, self.b)
        QWidget.setTabOrder(self.b, self.hold_seconds)
        QWidget.setTabOrder(self.hold_seconds, self.tabWidget_2)
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
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"\u4e0b\u8bfe\u540e\u591a\u957f\u65f6\u95f4\u5185\u4e0d\u53ef\u4ee5\u518d\u6b21\u6253\u5f00\u6559\u5b66\u8f6f\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6301\u7eed\u65f6\u95f4(\u79d2)", None))
#if QT_CONFIG(tooltip)
        self.if_tray_hide.setToolTip(QCoreApplication.translate("Form", u"\u5c06\u6258\u76d8\u56fe\u6807\u8bbe\u7f6e\u4e3a\u900f\u660e\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.if_tray_hide.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u6258\u76d8                                                                                      ", None))
#if QT_CONFIG(tooltip)
        self.b.setToolTip(QCoreApplication.translate("Form", u"\u5ef6\u8fdf\u6700\u5927\u503c", None))
#endif // QT_CONFIG(tooltip)
        self.if_strong_hide.setText(QCoreApplication.translate("Form", u"\u5f3a\u529b\u9690\u85cf\u6a21\u5f0f(\u8bf7\u4f7f\u7528ctrl+win+alt+shift+f6\u6253\u5f00\u8bbe\u7f6e, \u6258\u76d8\u56fe\u6807\u5c06\u6d88\u5931)", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"\u5f53\u4e0b\u8bfe\u540e\u4f1a\u968f\u673a\u5728\u8fd9\u4e2a\u8303\u56f4\u5185\u53d6\u503c\u4f5c\u4e3a\u5ef6\u8fdf, \u7136\u540e\u7b49\u5f85\u5ef6\u8fdf\u540e\u518d\u6740\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"\u968f\u673a\u7b49\u5f85\u65f6\u95f4(\u79d2)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"~", None))
#if QT_CONFIG(tooltip)
        self.a.setToolTip(QCoreApplication.translate("Form", u"\u5ef6\u8fdf\u6700\u5c0f\u503c", None))
#endif // QT_CONFIG(tooltip)
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
        self.label.setText(QCoreApplication.translate("Form", u"   \u90a3\u523b\u590f\uff01", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e00\u4f4d\u95f2\u7740\u6ca1\u4e8b\u7684\u521d\u4e09\u751f\u5199\u7684\u5c0f\u7a0b\u5e8f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.minimize_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.close_button.setText(QCoreApplication.translate("Form", u"\u00d7", None))
    # retranslateUi

