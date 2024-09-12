from PyQt6 import QtCore, QtGui, QtWidgets


class UiDialog(object):
    def __init__(self):
        self.title_text = None
        self.priority_text = None
        self.politics_image = None
        self.age_image = None
        self.name_image = None
        self.birthday_image = None
        self.tab = None
        self.tabWidget = None
        self.ok_button = None
        self.education_image = None
        self.phone_image = None
        self.school_image = None
        self.work_year_image = None
        self.user_image = None
        self.layoutWidget = None
        self.verticalLayout = None
        self.label = None
        self.label_2 = None
        self.label_3 = None
        self.label_17 = None
        self.label_4 = None
        self.label_7 = None
        self.label_5 = None
        self.label_6 = None
        self.layoutWidget1 = None
        self.verticalLayout_2 = None
        self.name_text = None
        self.birthday_text = None
        self.age_text = None
        self.political_text = None
        self.degree_text = None
        self.phone_text = None
        self.school_text = None
        self.work_year_text = None
        self.tab_2 = None
        self.label_9 = None
        self.player_label2_text = None
        self.player_label1_text = None
        self.label_13 = None
        self.match_position_text = None
        self.label_1 = None
        self.label_0 = None
        self.salary_text = None
        self.label_image = None
        self.salary_image = None
        self.work_image = None
        self.priority_image = None
        self.player_label3_text = None
        self.match_position_image = None

    def setup_ui(self, dialog):
        times = 2
        dialog.setObjectName("dialog")
        dialog.resize(352 * times, 352 * times)
        dialog.setMinimumSize(QtCore.QSize(352 * times, 352 * times))
        dialog.setMaximumSize(QtCore.QSize(352 * times, 352 * times))
        self.ok_button = QtWidgets.QPushButton(parent=dialog)
        self.ok_button.setGeometry(QtCore.QRect(142 * times, 312 * times, 75 * times, 24 * times))
        self.ok_button.setObjectName("ok_button")
        self.tabWidget = QtWidgets.QTabWidget(parent=dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20 * times, 60 * times, 311 * times, 251 * times))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.birthday_image = QtWidgets.QLabel(parent=self.tab)
        self.birthday_image.setGeometry(QtCore.QRect(10 * times, 39 * times, 16 * times, 16 * times))
        self.birthday_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.birthday_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.birthday_image.setText("")
        self.birthday_image.setObjectName("birthday_image")
        self.name_image = QtWidgets.QLabel(parent=self.tab)
        self.name_image.setGeometry(QtCore.QRect(10 * times, 12 * times, 16 * times, 16 * times))
        self.name_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.name_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.name_image.setText("")
        self.name_image.setObjectName("name_image")
        self.age_image = QtWidgets.QLabel(parent=self.tab)
        self.age_image.setGeometry(QtCore.QRect(10 * times, 66 * times, 16 * times, 16 * times))
        self.age_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.age_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.age_image.setText("")
        self.age_image.setObjectName("age_image")
        self.politics_image = QtWidgets.QLabel(parent=self.tab)
        self.politics_image.setGeometry(QtCore.QRect(10 * times, 91 * times, 16 * times, 16 * times))
        self.politics_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.politics_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.politics_image.setText("")
        self.politics_image.setObjectName("politics_image")
        self.education_image = QtWidgets.QLabel(parent=self.tab)
        self.education_image.setGeometry(QtCore.QRect(10 * times, 116 * times, 16 * times, 16 * times))
        self.education_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.education_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.education_image.setText("")
        self.education_image.setObjectName("education_image")
        self.phone_image = QtWidgets.QLabel(parent=self.tab)
        self.phone_image.setGeometry(QtCore.QRect(10 * times, 142 * times, 16 * times, 16 * times))
        self.phone_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.phone_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.phone_image.setText("")
        self.phone_image.setObjectName("phone_image")
        self.school_image = QtWidgets.QLabel(parent=self.tab)
        self.school_image.setGeometry(QtCore.QRect(10 * times, 167 * times, 16 * times, 16 * times))
        self.school_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.school_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.school_image.setText("")
        self.school_image.setObjectName("school_image")
        self.work_year_image = QtWidgets.QLabel(parent=self.tab)
        self.work_year_image.setGeometry(QtCore.QRect(10 * times, 192 * times, 16 * times, 16 * times))
        self.work_year_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.work_year_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.work_year_image.setText("")
        self.work_year_image.setObjectName("work_year_image")
        self.user_image = QtWidgets.QLabel(parent=self.tab)
        self.user_image.setGeometry(QtCore.QRect(240 * times, 0 * times, 64 * times, 64 * times))
        self.user_image.setMinimumSize(QtCore.QSize(64 * times, 64 * times))
        self.user_image.setMaximumSize(QtCore.QSize(64 * times, 64 * times))
        self.user_image.setText("")
        self.user_image.setObjectName("user_image")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30 * times, 11 * times, 61 * times, 201 * times))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_17 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(100 * times, 11 * times, 141 * times, 201 * times))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.name_text.setObjectName("name_text")
        self.verticalLayout_2.addWidget(self.name_text)
        self.birthday_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.birthday_text.setObjectName("birthday_text")
        self.verticalLayout_2.addWidget(self.birthday_text)
        self.age_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.age_text.setObjectName("age_text")
        self.verticalLayout_2.addWidget(self.age_text)
        self.political_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.political_text.setObjectName("political_text")
        self.verticalLayout_2.addWidget(self.political_text)
        self.degree_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.degree_text.setObjectName("degree_text")
        self.verticalLayout_2.addWidget(self.degree_text)
        self.phone_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.phone_text.setObjectName("phone_text")
        self.verticalLayout_2.addWidget(self.phone_text)
        self.school_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.school_text.setMaximumSize(QtCore.QSize(140 * times, 16777215 * times))
        self.school_text.setObjectName("school_text")
        self.verticalLayout_2.addWidget(self.school_text)
        self.work_year_text = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.work_year_text.setObjectName("work_year_text")
        self.verticalLayout_2.addWidget(self.work_year_text)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30 * times, 10 * times, 54 * times, 16 * times))
        font = QtGui.QFont()
        font.setPointSize(10 * times)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.player_label2_text = QtWidgets.QLabel(parent=self.tab_2)
        self.player_label2_text.setGeometry(QtCore.QRect(120 * times, 40 * times, 61 * times, 16 * times))
        self.player_label2_text.setObjectName("player_label2_text")
        self.player_label1_text = QtWidgets.QLabel(parent=self.tab_2)
        self.player_label1_text.setGeometry(QtCore.QRect(40 * times, 40 * times, 71 * times, 16 * times))
        self.player_label1_text.setObjectName("player_label1_text")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30 * times, 130 * times, 54 * times, 16 * times))
        font = QtGui.QFont()
        font.setPointSize(10 * times)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.match_position_text = QtWidgets.QLabel(parent=self.tab_2)
        self.match_position_text.setGeometry(QtCore.QRect(50 * times, 160 * times, 54 * times, 16 * times))
        self.match_position_text.setObjectName("match_position_text")
        self.label_1 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_1.setGeometry(QtCore.QRect(180 * times, 158 * times, 81 * times, 20 * times))
        self.label_1.setObjectName("label_1")
        self.label_0 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_0.setGeometry(QtCore.QRect(30 * times, 70 * times, 54 * times, 16 * times))
        font = QtGui.QFont()
        font.setPointSize(10 * times)
        font.setBold(True)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.salary_text = QtWidgets.QLabel(parent=self.tab_2)
        self.salary_text.setGeometry(QtCore.QRect(40 * times, 100 * times, 111 * times, 16 * times))
        self.salary_text.setObjectName("salary_text")
        self.priority_text = QtWidgets.QLabel(parent=self.tab_2)
        self.priority_text.setGeometry(QtCore.QRect(255 * times, 160 * times, 31 * times, 16 * times))
        font = QtGui.QFont()
        font.setBold(True)
        self.priority_text.setFont(font)
        self.priority_text.setObjectName("priority_text")
        self.label_image = QtWidgets.QLabel(parent=self.tab_2)
        self.label_image.setGeometry(QtCore.QRect(10 * times, 10 * times, 16 * times, 16 * times))
        self.label_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.label_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.salary_image = QtWidgets.QLabel(parent=self.tab_2)
        self.salary_image.setGeometry(QtCore.QRect(10 * times, 70 * times, 16 * times, 16 * times))
        self.salary_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.salary_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.salary_image.setText("")
        self.salary_image.setObjectName("salary_image")
        self.work_image = QtWidgets.QLabel(parent=self.tab_2)
        self.work_image.setGeometry(QtCore.QRect(10 * times, 130 * times, 16 * times, 16 * times))
        self.work_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.work_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.work_image.setText("")
        self.work_image.setObjectName("work_image")
        self.priority_image = QtWidgets.QLabel(parent=self.tab_2)
        self.priority_image.setGeometry(QtCore.QRect(160 * times, 160 * times, 16 * times, 16 * times))
        self.priority_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.priority_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.priority_image.setText("")
        self.priority_image.setObjectName("priority_image")
        self.player_label3_text = QtWidgets.QLabel(parent=self.tab_2)
        self.player_label3_text.setGeometry(QtCore.QRect(190 * times, 40 * times, 81 * times, 16 * times))
        self.player_label3_text.setObjectName("player_label3_text")
        self.match_position_image = QtWidgets.QLabel(parent=self.tab_2)
        self.match_position_image.setGeometry(QtCore.QRect(30 * times, 160 * times, 16 * times, 16 * times))
        self.match_position_image.setMinimumSize(QtCore.QSize(16 * times, 16 * times))
        self.match_position_image.setMaximumSize(QtCore.QSize(16 * times, 16 * times))
        self.match_position_image.setText("")
        self.match_position_image.setObjectName("match_position_image")
        self.tabWidget.addTab(self.tab_2, "")
        self.title_text = QtWidgets.QLabel(parent=dialog)
        self.title_text.setGeometry(QtCore.QRect(110 * times, 8 * times, 151 * times, 41 * times))
        font = QtGui.QFont()
        font.setPointSize(12 * times)
        self.title_text.setFont(font)
        self.title_text.setObjectName("title_text")

        self.re_translate_ui(dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def re_translate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "解析结果"))
        self.ok_button.setText(_translate("dialog", "确定"))
        self.label.setText(_translate("dialog", "姓名"))
        self.label_2.setText(_translate("dialog", "出生年月"))
        self.label_3.setText(_translate("dialog", "年龄"))
        self.label_17.setText(_translate("dialog", "政治面貌"))
        self.label_4.setText(_translate("dialog", "学历"))
        self.label_7.setText(_translate("dialog", "电话"))
        self.label_5.setText(_translate("dialog", "毕业院校"))
        self.label_6.setText(_translate("dialog", "工作年限"))
        self.name_text.setText(_translate("dialog", "王雅顺"))
        self.birthday_text.setText(_translate("dialog", "1996.9.9"))
        self.age_text.setText(_translate("dialog", "28"))
        self.political_text.setText(_translate("dialog", "中共党员"))
        self.degree_text.setText(_translate("dialog", "大专"))
        self.phone_text.setText(_translate("dialog", "13800008888"))
        self.school_text.setText(_translate("dialog", "常州信息职业技术学院"))
        self.work_year_text.setText(_translate("dialog", "2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dialog", "基本信息"))
        self.label_9.setText(_translate("dialog", "选手标签"))
        self.player_label2_text.setText(_translate("dialog", "工作稳定"))
        self.player_label1_text.setText(_translate("dialog", "经验丰富"))
        self.label_13.setText(_translate("dialog", "岗位匹配"))
        self.match_position_text.setText(_translate("dialog", "市场营销"))
        self.label_1.setText(_translate("dialog", "匹配优先级："))
        self.label_0.setText(_translate("dialog", "预计薪酬"))
        self.salary_text.setText(_translate("dialog", "7000-10000元/月"))
        self.priority_text.setText(_translate("dialog", "高"))
        self.player_label3_text.setText(_translate("dialog", "英语能力良好"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dialog", "人才画像"))
        self.title_text.setText(_translate("dialog", "个人简历解析结果"))
