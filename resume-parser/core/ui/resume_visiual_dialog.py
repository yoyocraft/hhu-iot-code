from PyQt6 import QtCore, QtGui, QtWidgets


class UiDialog2(object):
    def __init__(self):
        self.title_text = None
        self.ok_button = None
        self.verticalLayout_4 = None
        self.verticalLayoutWidget = None
        self.tab_4 = None
        self.verticalLayout_3 = None
        self.verticalLayoutWidget_2 = None
        self.tab_3 = None
        self.verticalLayout_2 = None
        self.verticalLayoutWidget_3 = None
        self.tab_2 = None
        self.verticalLayout_1 = None
        self.verticalLayoutWidget_4 = None
        self.tab = None
        self.tabWidget = None

    def setup_ui(self, dialog2):
        times = 2
        dialog2.setObjectName("Dialog2")
        dialog2.resize(512 * times, 416 * times)
        dialog2.setMinimumSize(QtCore.QSize(512 * times, 416 * times))
        dialog2.setMaximumSize(QtCore.QSize(512 * times, 416 * times))
        self.tabWidget = QtWidgets.QTabWidget(parent=dialog2)
        self.tabWidget.setGeometry(QtCore.QRect(20 * times, 50 * times, 471 * times, 301 * times))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 451 * times, 271 * times))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 451 * times, 271 * times))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 451 * times, 271 * times))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451 * times, 271 * times))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.ok_button = QtWidgets.QPushButton(parent=dialog2)
        self.ok_button.setGeometry(QtCore.QRect(220 * times, 360 * times, 75 * times, 24 * times))
        self.ok_button.setObjectName("ok_button")
        self.title_text = QtWidgets.QLabel(parent=dialog2)
        self.title_text.setGeometry(QtCore.QRect(190 * times, 10 * times, 141 * times, 41 * times))
        font = QtGui.QFont()
        font.setPointSize(12 * times)
        self.title_text.setFont(font)
        self.title_text.setObjectName("title_text")

        self.re_translate_ui(dialog2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dialog2)

    def re_translate_ui(self, dialog2):
        _translate = QtCore.QCoreApplication.translate
        dialog2.setWindowTitle(_translate("dialog2", "Resume Statistics Visualization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dialog2", "Education Statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dialog2", "Age Statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("dialog2", "Alma Mater Statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("dialog2", "Years of Experience "
                                                                                            "Statistics"))
        self.ok_button.setText(_translate("dialog2", "OK"))
        self.title_text.setText(_translate("dialog2", "Resume Statistics Visualization"))

