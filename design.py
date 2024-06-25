# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QDateEdit,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(653, 743)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(653, 624))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calc_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"\n"
"    font-family: Jost;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"    }")
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.VerticalTabs)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_title = QHBoxLayout()
        self.horizontalLayout_title.setObjectName(u"horizontalLayout_title")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(500, 50))
        font = QFont()
        font.setFamilies([u"Jost"])
        font.setPointSize(16)
        font.setBold(True)
        self.title_label.setFont(font)

        self.horizontalLayout_title.addWidget(self.title_label)

        self.First_dateEdit = QDateEdit(self.centralwidget)
        self.First_dateEdit.setObjectName(u"First_dateEdit")
        self.First_dateEdit.setFont(font)
        self.First_dateEdit.setStyleSheet(u"")
        self.First_dateEdit.setWrapping(False)
        self.First_dateEdit.setFrame(False)
        self.First_dateEdit.setKeyboardTracking(True)
        self.First_dateEdit.setDateTime(QDateTime(QDate(2024, 1, 2), QTime(0, 0, 0)))
        self.First_dateEdit.setCalendarPopup(True)

        self.horizontalLayout_title.addWidget(self.First_dateEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_title)

        self.horizontalLayout_reason = QHBoxLayout()
        self.horizontalLayout_reason.setObjectName(u"horizontalLayout_reason")
        self.reason_label = QLabel(self.centralwidget)
        self.reason_label.setObjectName(u"reason_label")
        self.reason_label.setMaximumSize(QSize(500, 50))
        self.reason_label.setFont(font)

        self.horizontalLayout_reason.addWidget(self.reason_label)

        self.reason_lineEdit = QLineEdit(self.centralwidget)
        self.reason_lineEdit.setObjectName(u"reason_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.reason_lineEdit.sizePolicy().hasHeightForWidth())
        self.reason_lineEdit.setSizePolicy(sizePolicy1)
        self.reason_lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_reason.addWidget(self.reason_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_reason)

        self.horizontalLayout_date = QHBoxLayout()
        self.horizontalLayout_date.setObjectName(u"horizontalLayout_date")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_start_date = QHBoxLayout()
        self.horizontalLayout_start_date.setObjectName(u"horizontalLayout_start_date")
        self.start_label = QLabel(self.centralwidget)
        self.start_label.setObjectName(u"start_label")
        sizePolicy.setHeightForWidth(self.start_label.sizePolicy().hasHeightForWidth())
        self.start_label.setSizePolicy(sizePolicy)
        self.start_label.setMinimumSize(QSize(30, 0))
        self.start_label.setFont(font)
        self.start_label.setScaledContents(True)

        self.horizontalLayout_start_date.addWidget(self.start_label)

        self.start_dateEdit = QDateEdit(self.centralwidget)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setMinimumSize(QSize(165, 0))
        self.start_dateEdit.setFont(font)
        self.start_dateEdit.setStyleSheet(u"")
        self.start_dateEdit.setWrapping(False)
        self.start_dateEdit.setFrame(False)
        self.start_dateEdit.setKeyboardTracking(True)
        self.start_dateEdit.setDateTime(QDateTime(QDate(2024, 1, 3), QTime(0, 0, 0)))
        self.start_dateEdit.setCalendarPopup(True)

        self.horizontalLayout_start_date.addWidget(self.start_dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_start_date)

        self.horizontalLayout_end_date = QHBoxLayout()
        self.horizontalLayout_end_date.setObjectName(u"horizontalLayout_end_date")
        self.end_label = QLabel(self.centralwidget)
        self.end_label.setObjectName(u"end_label")
        sizePolicy.setHeightForWidth(self.end_label.sizePolicy().hasHeightForWidth())
        self.end_label.setSizePolicy(sizePolicy)
        self.end_label.setMinimumSize(QSize(30, 0))
        self.end_label.setFont(font)
        self.end_label.setScaledContents(True)

        self.horizontalLayout_end_date.addWidget(self.end_label)

        self.end_dateEdit = QDateEdit(self.centralwidget)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        self.end_dateEdit.setMinimumSize(QSize(165, 0))
        self.end_dateEdit.setFont(font)
        self.end_dateEdit.setStyleSheet(u"")
        self.end_dateEdit.setWrapping(False)
        self.end_dateEdit.setFrame(False)
        self.end_dateEdit.setKeyboardTracking(True)
        self.end_dateEdit.setDateTime(QDateTime(QDate(2024, 1, 4), QTime(0, 0, 0)))
        self.end_dateEdit.setCalendarPopup(True)

        self.horizontalLayout_end_date.addWidget(self.end_dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_end_date)


        self.horizontalLayout_date.addLayout(self.verticalLayout)

        self.add_pushButton = QPushButton(self.centralwidget)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMaximumSize(QSize(400, 70))
        font1 = QFont()
        font1.setFamilies([u"Jost"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.add_pushButton.setFont(font1)
        self.add_pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_pushButton.setStyleSheet(u" QPushButton {\n"
"     border: 2px solid #8AB4F8;\n"
"     border-radius: 10px;\n"
"     min-width: 80px;\n"
"	font-size: 15pt;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     background-color: #8AB4F8;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     border: 2px solid #9AA0A6;\n"
"     background-color: #9AA0A6;\n"
" }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add_date.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_pushButton.setIcon(icon1)
        self.add_pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_date.addWidget(self.add_pushButton)

        self.del_pushButton = QPushButton(self.centralwidget)
        self.del_pushButton.setObjectName(u"del_pushButton")
        self.del_pushButton.setMaximumSize(QSize(400, 70))
        self.del_pushButton.setFont(font1)
        self.del_pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.del_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.del_pushButton.setStyleSheet(u" QPushButton {\n"
"     border: 2px solid #8AB4F8;\n"
"     border-radius: 10px;\n"
"     min-width: 80px;\n"
"	font-size: 15pt;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     background-color: #8AB4F8;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     border: 2px solid #9AA0A6;\n"
"     background-color: #9AA0A6;\n"
" }\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/backspace.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.del_pushButton.setIcon(icon2)
        self.del_pushButton.setIconSize(QSize(32, 32))
        self.del_pushButton.setAutoRepeat(False)
        self.del_pushButton.setAutoExclusive(False)
        self.del_pushButton.setAutoDefault(False)

        self.horizontalLayout_date.addWidget(self.del_pushButton)

        self.del_all_pushButton = QPushButton(self.centralwidget)
        self.del_all_pushButton.setObjectName(u"del_all_pushButton")
        self.del_all_pushButton.setMaximumSize(QSize(400, 70))
        self.del_all_pushButton.setFont(font1)
        self.del_all_pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.del_all_pushButton.setStyleSheet(u" QPushButton {\n"
"     border: 2px solid #8AB4F8;\n"
"     border-radius: 10px;\n"
"     min-width: 80px;\n"
"	font-size: 15pt;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     background-color: #8AB4F8;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     border: 2px solid #9AA0A6;\n"
"     background-color: #9AA0A6;\n"
" }\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/del_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.del_all_pushButton.setIcon(icon3)
        self.del_all_pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_date.addWidget(self.del_all_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_date)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(0, 200))
        self.tableWidget.setStyleSheet(u"\n"
"\n"
"QTableView::section {\n"
"	background-color: rgba(53,53,53, 50);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"	wight: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	boder-radius: 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	border: 2px solid #8AB4F8;\n"
"	background-color: rgb(255, 255, 255);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background-color: #8AB4F8;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"	border: 2px solid  #9aa0a6;\n"
"	background-color: #9aa0a6;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"	wight: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	b"
                        "oder-radius: 0;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	border: 2px solid #8AB4F8;\n"
"	background-color: rgb(255, 255, 255);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background-color: #8AB4F8;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"	border: 2px solid  #9aa0a6;\n"
"	background-color: #9aa0a6;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout_max_days = QHBoxLayout()
        self.horizontalLayout_max_days.setSpacing(6)
        self.horizontalLayout_max_days.setObjectName(u"horizontalLayout_max_days")
        self.horizontalLayout_max_days.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_max_days.setContentsMargins(0, 0, 0, 0)
        self.max_days_label = QLabel(self.centralwidget)
        self.max_days_label.setObjectName(u"max_days_label")
        sizePolicy.setHeightForWidth(self.max_days_label.sizePolicy().hasHeightForWidth())
        self.max_days_label.setSizePolicy(sizePolicy)
        self.max_days_label.setMaximumSize(QSize(16777215, 16777215))
        self.max_days_label.setFont(font)
        self.max_days_label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.max_days_label.setTabletTracking(False)
        self.max_days_label.setScaledContents(True)
        self.max_days_label.setWordWrap(True)

        self.horizontalLayout_max_days.addWidget(self.max_days_label)

        self.max_days_spinBox = QSpinBox(self.centralwidget)
        self.max_days_spinBox.setObjectName(u"max_days_spinBox")
        self.max_days_spinBox.setMaximumSize(QSize(100, 70))
        self.max_days_spinBox.setStyleSheet(u"\n"
"QSpinBox {\n"
"background-color: rgba(149, 185, 240, 50);\n"
"border: 1px solid #0078d7;\n"
"border-radius: 10px;\n"
"font-family: Jost;\n"
"font-size: 28pt;\n"
"}")
        self.max_days_spinBox.setFrame(False)
        self.max_days_spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.max_days_spinBox.setKeyboardTracking(True)
        self.max_days_spinBox.setMaximum(999)
        self.max_days_spinBox.setValue(59)

        self.horizontalLayout_max_days.addWidget(self.max_days_spinBox)

        self.result_pushButton = QPushButton(self.centralwidget)
        self.result_pushButton.setObjectName(u"result_pushButton")
        self.result_pushButton.setMaximumSize(QSize(400, 70))
        font2 = QFont()
        font2.setFamilies([u"Jost"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.result_pushButton.setFont(font2)
        self.result_pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.result_pushButton.setStyleSheet(u" QPushButton {\n"
"     border: 2px solid #8AB4F8;\n"
"     border-radius: 10px;\n"
"     min-width: 80px;\n"
"	font-size: 20pt;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     background-color: #8AB4F8;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     border: 2px solid #9AA0A6;\n"
"     background-color: #9AA0A6;\n"
" }\n"
"")
        self.result_pushButton.setIcon(icon)
        self.result_pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_max_days.addWidget(self.result_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_max_days)

        self.horizontalLayout_result = QHBoxLayout()
        self.horizontalLayout_result.setObjectName(u"horizontalLayout_result")
        self.horizontalLayout_result.setSizeConstraint(QLayout.SetMaximumSize)
        self.result_title_label = QLabel(self.centralwidget)
        self.result_title_label.setObjectName(u"result_title_label")
        sizePolicy.setHeightForWidth(self.result_title_label.sizePolicy().hasHeightForWidth())
        self.result_title_label.setSizePolicy(sizePolicy)
        self.result_title_label.setMinimumSize(QSize(0, 150))
        self.result_title_label.setFont(font)
        self.result_title_label.setScaledContents(True)
        self.result_title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.result_title_label.setWordWrap(True)

        self.horizontalLayout_result.addWidget(self.result_title_label)

        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        sizePolicy.setHeightForWidth(self.result_label.sizePolicy().hasHeightForWidth())
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setMinimumSize(QSize(200, 0))
        font3 = QFont()
        font3.setFamilies([u"Jost"])
        font3.setPointSize(28)
        font3.setBold(True)
        self.result_label.setFont(font3)
        self.result_label.setStyleSheet(u"font-size: 28pt;")
        self.result_label.setScaledContents(True)
        self.result_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_result.addWidget(self.result_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_result)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DateCalculator", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0438\u0441\u043a\u0430:", None))
        self.First_dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.reason_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430 \u043f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438:", None))
        self.reason_lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0430", None))
        self.start_label.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.start_dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.end_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e", None))
        self.end_dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.add_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.del_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c\n"
"\u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.del_all_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c\n"
"\u0432\u0441\u0451", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430                 ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043d\u0435\u0439         ", None));
        self.max_days_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043d\u0435\u0439", None))
        self.result_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0451\u0442", None))
        self.result_title_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043d\u0435\u0441\u0442\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u0434\u043e:", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"01.02.2024", None))
    # retranslateUi

