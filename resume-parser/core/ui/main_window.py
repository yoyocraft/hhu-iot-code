from PyQt6 import QtCore, QtGui, QtWidgets


class UiWidget(object):
    def __init__(self):
        self.parse_button1 = None
        self.parse_button2 = None
        self.select_button = None
        self.tab_3 = None
        self.tab_4 = None
        self.tabWidget = None
        self.title_text = None
        self.file_path_label = None
        self.progressBar = None

    def setup_ui(self, widget):
        times = 2
        widget.setObjectName("widget")
        widget.resize(352 * times, 352 * times)
        widget.setMinimumSize(QtCore.QSize(352 * times, 352 * times))
        widget.setMaximumSize(QtCore.QSize(352 * times, 352 * times))
        self.progressBar = QtWidgets.QProgressBar(parent=widget)
        self.progressBar.setGeometry(QtCore.QRect(40 * times, 320 * times, 271 * times, 23 * times))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.file_path_label = QtWidgets.QLabel(parent=widget)
        self.file_path_label.setGeometry(QtCore.QRect(40 * times, 280 * times, 271 * times, 31 * times))
        self.file_path_label.setMaximumSize(QtCore.QSize(16777215 * times, 48 * times))
        self.file_path_label.setLineWidth(1)
        self.file_path_label.setWordWrap(True)
        self.file_path_label.setObjectName("file_path_label")
        self.title_text = QtWidgets.QLabel(parent=widget)
        self.title_text.setGeometry(QtCore.QRect(100 * times, 10 * times, 171 * times, 41 * times))
        font = QtGui.QFont()
        font.setPointSize(14 * times)
        self.title_text.setFont(font)
        self.title_text.setObjectName("title_text")
        self.tabWidget = QtWidgets.QTabWidget(parent=widget)
        self.tabWidget.setGeometry(QtCore.QRect(30 * times, 60 * times, 291 * times, 211 * times))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.select_button = QtWidgets.QPushButton(parent=self.tab_3)
        self.select_button.setGeometry(QtCore.QRect(20 * times, 10 * times, 251 * times, 131 * times))
        self.select_button.setObjectName("select_button")
        self.parse_button1 = QtWidgets.QPushButton(parent=self.tab_3)
        self.parse_button1.setGeometry(QtCore.QRect(100 * times, 150 * times, 101 * times, 24 * times))
        self.parse_button1.setObjectName("parse_button1")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.re_translate_ui(widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def re_translate_ui(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Resume Parser"))
        self.file_path_label.setText(_translate("widget", " "))
        self.title_text.setText(_translate("widget", "Resume Parser System"))
        self.select_button.setText(_translate("widget", "upload"))
        self.parse_button1.setText(_translate("widget", "parse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("widget", "File Uploader"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("widget", "stay tuned..."))
        self.tabWidget.setTabEnabled(self.tabWidget.indexOf(self.tab_4), False)
