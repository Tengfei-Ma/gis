# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1113, 847)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/global.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1111, 821))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.line_2 = QtWidgets.QFrame(parent=self.tab_1)
        self.line_2.setGeometry(QtCore.QRect(0, 300, 1101, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.pushButton_1 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_1.setGeometry(QtCore.QRect(80, 10, 101, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 10, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_1 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_1.setGeometry(QtCore.QRect(80, 320, 91, 31))
        self.label_1.setObjectName("label_1")
        self.listWidget = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget.setGeometry(QtCore.QRect(80, 60, 331, 191))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_2.setGeometry(QtCore.QRect(700, 60, 331, 191))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(80, 470, 81, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.tab_1)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 480, 81, 31))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 750, 71, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.progressBar = QtWidgets.QProgressBar(parent=self.tab_1)
        self.progressBar.setGeometry(QtCore.QRect(310, 750, 491, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 260, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(940, 260, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox = QtWidgets.QSpinBox(parent=self.tab_1)
        self.spinBox.setGeometry(QtCore.QRect(80, 580, 161, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.tab_1)
        self.tabWidget_2.setGeometry(QtCore.QRect(330, 480, 181, 181))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.tab_21)
        self.spinBox_4.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.tab_21)
        self.spinBox_5.setGeometry(QtCore.QRect(10, 70, 151, 22))
        self.spinBox_5.setObjectName("spinBox_5")
        self.tabWidget_2.addTab(self.tab_21, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_22)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_22)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.label_11.setObjectName("label_11")
        self.comboBox = QtWidgets.QComboBox(parent=self.tab_22)
        self.comboBox.setGeometry(QtCore.QRect(70, 20, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.tab_22)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 60, 71, 22))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.tab_22)
        self.doubleSpinBox.setGeometry(QtCore.QRect(10, 100, 131, 22))
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMaximum(99999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.tabWidget_2.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.label_14 = QtWidgets.QLabel(parent=self.tab_23)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.tab_23)
        self.label_15.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.tab_23)
        self.spinBox_6.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.spinBox_6.setMaximum(9999999)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(parent=self.tab_23)
        self.spinBox_7.setGeometry(QtCore.QRect(10, 60, 151, 22))
        self.spinBox_7.setObjectName("spinBox_7")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(parent=self.tab_23)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(10, 100, 151, 22))
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setMaximum(99999.99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.tabWidget_2.addTab(self.tab_23, "")
        self.listWidget_5 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_5.setGeometry(QtCore.QRect(160, 330, 81, 131))
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(270, 320, 61, 31))
        self.label_2.setObjectName("label_2")
        self.listWidget_6 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_6.setGeometry(QtCore.QRect(330, 330, 181, 131))
        self.listWidget_6.setObjectName("listWidget_6")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_8.setGeometry(QtCore.QRect(270, 470, 61, 31))
        self.label_8.setObjectName("label_8")
        self.line_1 = QtWidgets.QFrame(parent=self.tab_1)
        self.line_1.setGeometry(QtCore.QRect(540, 330, 20, 391))
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_1.setLineWidth(3)
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_1.setObjectName("line_1")
        self.label_20 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_20.setGeometry(QtCore.QRect(80, 690, 81, 31))
        self.label_20.setObjectName("label_20")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.tab_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 690, 391, 31))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.tab_1)
        self.lineEdit_4.setGeometry(QtCore.QRect(650, 690, 381, 31))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_21 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_21.setGeometry(QtCore.QRect(560, 690, 81, 31))
        self.label_21.setObjectName("label_21")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_15.setGeometry(QtCore.QRect(960, 750, 71, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_16.setGeometry(QtCore.QRect(760, 330, 101, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.tab_1)
        self.spinBox_2.setGeometry(QtCore.QRect(80, 630, 161, 31))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.tab_1)
        self.spinBox_3.setGeometry(QtCore.QRect(80, 530, 161, 31))
        self.spinBox_3.setMaximum(100)
        self.spinBox_3.setSingleStep(5)
        self.spinBox_3.setObjectName("spinBox_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.tab_1)
        self.plainTextEdit.setGeometry(QtCore.QRect(620, 400, 411, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        self.comboBox_3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "系统原型"))
        self.pushButton_1.setText(_translate("mainWindow", "选择 shp 数据源"))
        self.pushButton_2.setText(_translate("mainWindow", "选择 tif 数据源"))
        self.label_1.setText(_translate("mainWindow", "选择目标字段"))
        self.label_3.setText(_translate("mainWindow", "选择回归模型"))
        self.comboBox_2.setCurrentText(_translate("mainWindow", "RF"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "RF"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "SVM"))
        self.comboBox_2.setItemText(2, _translate("mainWindow", "XGBoost"))
        self.pushButton_6.setText(_translate("mainWindow", "开始训练"))
        self.pushButton_3.setText(_translate("mainWindow", "重置"))
        self.pushButton_4.setText(_translate("mainWindow", "重置"))
        self.spinBox.setPrefix(_translate("mainWindow", "BootstrapTimes  "))
        self.spinBox_4.setPrefix(_translate("mainWindow", "n_estimators： "))
        self.spinBox_5.setPrefix(_translate("mainWindow", "max_features： "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_21), _translate("mainWindow", "RF"))
        self.label_10.setText(_translate("mainWindow", "kernel  ："))
        self.label_11.setText(_translate("mainWindow", "gamma："))
        self.comboBox.setItemText(0, _translate("mainWindow", "rbf"))
        self.comboBox.setItemText(1, _translate("mainWindow", "linear"))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "scale"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "auto"))
        self.doubleSpinBox.setPrefix(_translate("mainWindow", "C        ：  "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_22), _translate("mainWindow", "SVM"))
        self.spinBox_6.setPrefix(_translate("mainWindow", "n_estimators： "))
        self.spinBox_7.setPrefix(_translate("mainWindow", "max_depth  ： "))
        self.doubleSpinBox_2.setPrefix(_translate("mainWindow", "learning_rate："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_23), _translate("mainWindow", "XGBoost"))
        self.label_2.setText(_translate("mainWindow", "任务队列"))
        self.label_8.setText(_translate("mainWindow", "参数设置"))
        self.label_20.setText(_translate("mainWindow", "模型保存至"))
        self.lineEdit_3.setPlaceholderText(_translate("mainWindow", "默认保存至 tif 数据源所在根目录的 output 文件夹"))
        self.lineEdit_4.setPlaceholderText(_translate("mainWindow", "默认保存至 tif 数据源所在根目录的 output 文件夹"))
        self.label_21.setText(_translate("mainWindow", "目标 tif 保存至"))
        self.pushButton_15.setText(_translate("mainWindow", "预测出图"))
        self.pushButton_16.setText(_translate("mainWindow", "导入模型文件"))
        self.spinBox_2.setSuffix(_translate("mainWindow", " 的模型"))
        self.spinBox_2.setPrefix(_translate("mainWindow", "保留Top "))
        self.spinBox_3.setSuffix(_translate("mainWindow", " %"))
        self.spinBox_3.setPrefix(_translate("mainWindow", "验证集占比 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("mainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "其它"))
