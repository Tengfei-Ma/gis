import math
import os.path

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QListWidgetItem, QCheckBox
from core.train import getFieldsFromShp
from core.train import trainShp


class Ui_mainWindow(QMainWindow):
    def __init__(self):
        super(Ui_mainWindow, self).__init__()
        self.listWidget_2_set = set()
        self.listWidget_4_set = set()
        self.listWidget_5_set = set()
        self.fields = {}
        self.setupUi(self)

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
        self.line_1 = QtWidgets.QFrame(parent=self.tab_1)
        self.line_1.setGeometry(QtCore.QRect(0, 320, 1101, 16))
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_1.setLineWidth(3)
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QFrame(parent=self.tab_1)
        self.line_2.setGeometry(QtCore.QRect(543, 340, 20, 371))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setObjectName("line_2")
        self.pushButton_1 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 10, 111, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 10, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget_1 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_1.setGeometry(QtCore.QRect(50, 60, 481, 191))
        self.listWidget_1.setObjectName("listWidget_1")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 270, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(970, 270, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_2.setGeometry(QtCore.QRect(580, 60, 481, 191))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label1 = QtWidgets.QLabel(parent=self.tab_1)
        self.label1.setGeometry(QtCore.QRect(50, 340, 81, 31))
        self.label1.setObjectName("label1")
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_3.setGeometry(QtCore.QRect(50, 370, 181, 121))
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 410, 81, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.listWidget_4 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_4.setGeometry(QtCore.QRect(330, 370, 191, 121))
        self.listWidget_4.setObjectName("listWidget_4")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(350, 340, 81, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_1 = QtWidgets.QComboBox(parent=self.tab_1)
        self.comboBox_1.setGeometry(QtCore.QRect(140, 510, 91, 22))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(52, 505, 71, 31))
        self.label_3.setObjectName("label_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.tab_1)
        self.tabWidget_2.setGeometry(QtCore.QRect(330, 510, 201, 151))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.spinBox_1 = QtWidgets.QSpinBox(parent=self.tab_21)
        self.spinBox_1.setGeometry(QtCore.QRect(20, 10, 151, 22))
        self.spinBox_1.setMinimum(50)
        self.spinBox_1.setMaximum(2000)
        self.spinBox_1.setSingleStep(50)
        self.spinBox_1.setObjectName("spinBox_1")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.tab_21)
        self.spinBox_2.setGeometry(QtCore.QRect(20, 50, 151, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.tab_21)
        self.spinBox_3.setGeometry(QtCore.QRect(20, 90, 151, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.tabWidget_2.addTab(self.tab_21, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.tab_22)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 10, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_22)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_22)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.tab_22)
        self.comboBox_3.setGeometry(QtCore.QRect(80, 50, 91, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(parent=self.tab_22)
        self.doubleSpinBox_1.setGeometry(QtCore.QRect(20, 90, 151, 22))
        self.doubleSpinBox_1.setSuffix("")
        self.doubleSpinBox_1.setDecimals(5)
        self.doubleSpinBox_1.setMinimum(1e-05)
        self.doubleSpinBox_1.setMaximum(99.99999)
        self.doubleSpinBox_1.setProperty("value", 1e-05)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.tabWidget_2.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.tab_23)
        self.spinBox_4.setGeometry(QtCore.QRect(20, 10, 151, 22))
        self.spinBox_4.setMinimum(50)
        self.spinBox_4.setMaximum(2000)
        self.spinBox_4.setSingleStep(50)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.tab_23)
        self.spinBox_5.setGeometry(QtCore.QRect(20, 50, 151, 22))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setObjectName("spinBox_5")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(parent=self.tab_23)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(20, 90, 151, 22))
        self.doubleSpinBox_2.setSuffix("")
        self.doubleSpinBox_2.setDecimals(5)
        self.doubleSpinBox_2.setMinimum(1e-05)
        self.doubleSpinBox_2.setMaximum(99.99999)
        self.doubleSpinBox_2.setProperty("value", 1e-05)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.tabWidget_2.addTab(self.tab_23, "")
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.tab_1)
        self.spinBox_6.setGeometry(QtCore.QRect(50, 550, 181, 21))
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(100)
        self.spinBox_6.setSingleStep(5)
        self.spinBox_6.setProperty("value", 5)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(parent=self.tab_1)
        self.spinBox_7.setGeometry(QtCore.QRect(50, 590, 181, 21))
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(100)
        self.spinBox_7.setSingleStep(1)
        self.spinBox_7.setProperty("value", 1)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(parent=self.tab_1)
        self.spinBox_8.setGeometry(QtCore.QRect(50, 630, 181, 21))
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(999)
        self.spinBox_8.setSingleStep(1)
        self.spinBox_8.setProperty("value", 1)
        self.spinBox_8.setMaximum(self.spinBox_7.value())
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(50, 680, 101, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(150, 680, 341, 31))
        self.label_7.setStyleSheet("border: 1px solid black;")
        self.label_7.setObjectName("label_7")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 680, 31, 31))
        self.pushButton_6.setIcon(QtGui.QIcon("../resource/save.png"))
        self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_6.setStyleSheet("border: none;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 740, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.progressBar = QtWidgets.QProgressBar(parent=self.tab_1)
        self.progressBar.setGeometry(QtCore.QRect(200, 740, 721, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_8.setGeometry(QtCore.QRect(770, 350, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.listWidget_5 = QtWidgets.QListWidget(parent=self.tab_1)
        self.listWidget_5.setGeometry(QtCore.QRect(580, 390, 481, 121))
        self.listWidget_5.setObjectName("listWidget_5")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_9.setGeometry(QtCore.QRect(970, 530, 91, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_8.setGeometry(QtCore.QRect(590, 610, 101, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(690, 610, 331, 31))
        self.label_9.setStyleSheet("border: 1px solid black;")
        self.label_9.setObjectName("label_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_10.setGeometry(QtCore.QRect(1030, 610, 31, 31))
        self.pushButton_10.setIcon(QtGui.QIcon("../resource/save.png"))
        self.pushButton_10.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_10.setStyleSheet("border: none;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_12.setGeometry(QtCore.QRect(970, 740, 91, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_10.setGeometry(QtCore.QRect(590, 680, 91, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_11.setGeometry(QtCore.QRect(690, 680, 331, 31))
        self.label_11.setStyleSheet("border: 1px solid black;")
        self.label_11.setObjectName("label_11")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton_11.setGeometry(QtCore.QRect(1030, 680, 31, 31))
        self.pushButton_11.setIcon(QtGui.QIcon("../resource/save.png"))
        self.pushButton_11.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_11.setStyleSheet("border: none;")
        self.pushButton_11.setObjectName("pushButton_11")
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
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.pushButton_1.clicked.connect(self.button1clicked)
        self.pushButton_2.clicked.connect(self.button2clicked)
        self.pushButton_3.clicked.connect(self.button3clicked)
        self.pushButton_4.clicked.connect(self.button4clicked)
        self.pushButton_5.clicked.connect(self.button5clicked)
        self.comboBox_1.currentIndexChanged.connect(self.combobox1changed)
        self.tabWidget_2.currentChanged.connect(self.tabWidget2changed)
        self.spinBox_7.valueChanged.connect(self.spinbox7changed)
        self.pushButton_6.clicked.connect(self.button6clicked)
        self.pushButton_8.clicked.connect(self.button8clicked)
        self.pushButton_9.clicked.connect(self.button9clicked)
        self.pushButton_10.clicked.connect(self.button10clicked)
        self.pushButton_11.clicked.connect(self.button11clicked)
        self.pushButton_7.clicked.connect(self.button7clicked)

    def button7clicked(self):
        if self.listWidget_1.count() == 0:
            QMessageBox.warning(None, "警告", "请选择shp数据源！")
            return
        if self.listWidget_2.count() < 2:
            QMessageBox.warning(None, "警告", "请继续添加tif数据源！")
            return
        if self.listWidget_3.count() == 0:
            QMessageBox.warning(None, "警告", "请选择目标字段并生成任务！")
            return
        if self.label_7.text() == "":
            QMessageBox.warning(None, "警告", "请选择模型保存目录！")
            return
        shpPath = self.listWidget_1.item(0).text()
        tifFiles = []
        for i in range(self.listWidget_2.count()):
            tifFiles.append(self.listWidget_2.item(i).text())
        tasks = []
        for i in range(self.listWidget_4.count()):
            tasks.append(self.listWidget_4.item(i).text())
        modelIndex = self.comboBox_1.currentIndex()
        modelArgs = []
        if modelIndex == 0:
            modelArgs.append(self.spinBox_1.value())
            modelArgs.append(self.spinBox_2.value())
            modelArgs.append(self.spinBox_3.value())
        elif modelIndex == 1:
            modelArgs.append(self.comboBox_2.currentText())
            if self.comboBox_3.currentText() == "scale" or self.comboBox_3.currentText() == "auto":
                modelArgs.append(self.comboBox_3.currentText())
            else:
                modelArgs.append(float(self.comboBox_3.currentText()))
            modelArgs.append(self.doubleSpinBox_1.value())
        elif modelIndex == 2:
            modelArgs.append(self.spinBox_4.value())
            modelArgs.append(self.spinBox_5.value())
            modelArgs.append(self.doubleSpinBox_2.value())
        else:
            return
        valRatio = self.spinBox_6.value() / 100
        trainTimes = self.spinBox_7.value()
        k = self.spinBox_8.value()
        modelDir = self.label_7.text()
        self.progressBar.setVisible(True)
        res = trainShp(shpPath, tifFiles, tasks, modelIndex, modelArgs, valRatio, trainTimes, k, modelDir,self.progressBar)
        if res == 1:
            self.progressBar.setValue(100)
            self.statusbar.showMessage("训练完毕！", 10000)
            QMessageBox.information(None, "消息提示", "训练完成，模型保存至指定目录！")
            self.progressBar.setVisible(False)
        else:
            QMessageBox.critical(None, "运行错误", "训练过程异常，请确认相关参数重新训练！")
            self.progressBar.setVisible(False)
    def button11clicked(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.Directory)
        if fd.exec():
            self.label_11.clear()
            self.label_11.setText(fd.selectedFiles()[0])

    def button10clicked(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setNameFilter('tif文件(*.tif)')
        if fd.exec():
            self.label_9.clear()
            self.label_9.setText(fd.selectedFiles()[0])

    def button9clicked(self):
        self.listWidget_5.clear()
        self.listWidget_5_set.clear()

    def button8clicked(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFiles)
        fd.setNameFilter('pkl文件(*.pkl)')
        if fd.exec():
            files = fd.selectedFiles()
            for file in files:
                if file not in self.listWidget_5_set:
                    if (len(self.listWidget_5_set) == 0 or
                            os.path.dirname(file) == os.path.dirname(list(self.listWidget_5_set)[0])):
                        item = QListWidgetItem(QtGui.QIcon("../resource/model.png"), file)
                        self.listWidget_5.addItem(item)
                        self.listWidget_5_set.add(file)
                    else:
                        QMessageBox.warning(None, "警告", "您选择的模型与已导入模型可能来自不同字段，请重新导入！")
                        return

    def button6clicked(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.Directory)
        if fd.exec():
            self.label_7.clear()
            self.label_7.setText(fd.selectedFiles()[0])

    def spinbox7changed(self, value):
        self.spinBox_8.setMaximum(value)

    def tabWidget2changed(self, index):
        self.comboBox_1.setCurrentIndex(index)

    def combobox1changed(self, index):
        self.tabWidget_2.setCurrentIndex(index)

    def button5clicked(self):
        self.listWidget_4.clear()
        for key, val in self.fields.items():
            if val == 1:
                item = QListWidgetItem(QtGui.QIcon("../resource/flag.png"), key)
                self.listWidget_4.addItem(item)

    def checkbox_state_changed(self, state):
        checkbox = self.sender()  # 获取发送信号的复选框对象
        field_name = checkbox.text()
        if state == 2:
            self.fields[field_name] = 1
        elif state == 0:
            self.fields[field_name] = 0

    def button4clicked(self):
        self.listWidget_2.clear()
        self.listWidget_2_set.clear()
        self.spinBox_3.setValue(1)
        self.spinBox_5.setValue(1)

    def button3clicked(self):
        self.listWidget_1.clear()

    def button2clicked(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFiles)
        fd.setNameFilter('tif文件(*.tif)')
        if fd.exec():
            files = fd.selectedFiles()
            for file in files:
                if file not in self.listWidget_2_set:
                    item = QListWidgetItem(QtGui.QIcon("../resource/shp_ds.png"), file)
                    self.listWidget_2.addItem(item)
                    self.listWidget_2_set.add(file)
            self.spinBox_3.setValue(math.ceil(math.sqrt(len(self.listWidget_2_set))))
            self.spinBox_5.setValue(math.ceil(math.sqrt(len(self.listWidget_2_set))))

    def button1clicked(self):
        if self.listWidget_1.count() > 0:
            QMessageBox.warning(None, "警告", "只能选择一个shp文件！")
            return
        else:
            fd = QFileDialog()
            fd.setFileMode(QFileDialog.FileMode.ExistingFile)
            fd.setNameFilter('shp文件(*.shp)')
            if fd.exec():
                files = fd.selectedFiles()
                item = QListWidgetItem(QtGui.QIcon("../resource/shp_ds.png"), files[0])
                self.listWidget_1.addItem(item)
                fields = getFieldsFromShp(files[0])
                for field in fields:
                    checkboxItem = QListWidgetItem()
                    checkbox = QCheckBox(field)
                    checkbox.stateChanged.connect(self.checkbox_state_changed)
                    checkboxItem.setSizeHint(checkbox.sizeHint())  # Set item size to match checkbox size
                    self.listWidget_3.addItem(checkboxItem)
                    self.listWidget_3.setItemWidget(checkboxItem, checkbox)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "系统原型"))
        self.pushButton_1.setText(_translate("mainWindow", "选择 shp 数据源"))
        self.pushButton_2.setText(_translate("mainWindow", "选择 tif 数据源"))
        self.pushButton_3.setText(_translate("mainWindow", "重置"))
        self.pushButton_4.setText(_translate("mainWindow", "重置"))
        self.label1.setText(_translate("mainWindow", "选择目标字段"))
        self.pushButton_5.setText(_translate("mainWindow", "生成任务"))
        self.label_2.setText(_translate("mainWindow", "任务队列"))
        self.comboBox_1.setItemText(0, _translate("mainWindow", "RF"))
        self.comboBox_1.setItemText(1, _translate("mainWindow", "SVM"))
        self.comboBox_1.setItemText(2, _translate("mainWindow", "XGBoost"))
        self.label_3.setText(_translate("mainWindow", "选择回归模型"))
        self.spinBox_1.setPrefix(_translate("mainWindow", "树的个数："))
        self.spinBox_2.setPrefix(_translate("mainWindow", "最大特征数："))
        self.spinBox_3.setPrefix(_translate("mainWindow", "树的深度："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_21), _translate("mainWindow", "RF"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "rbf"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "linear"))
        self.label_4.setText(_translate("mainWindow", "kernel："))
        self.label_5.setText(_translate("mainWindow", "gamma："))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "scale"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "auto"))
        self.doubleSpinBox_1.setPrefix(_translate("mainWindow", "C：          "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_22), _translate("mainWindow", "SVM"))
        self.spinBox_4.setPrefix(_translate("mainWindow", "树的个数："))
        self.spinBox_5.setPrefix(_translate("mainWindow", "树的深度："))
        self.doubleSpinBox_2.setPrefix(_translate("mainWindow", "学习率   ："))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_23), _translate("mainWindow", "XGBoost"))
        self.spinBox_6.setSuffix(_translate("mainWindow", " %"))
        self.spinBox_6.setPrefix(_translate("mainWindow", "验证集占比：        "))
        self.spinBox_7.setSuffix(_translate("mainWindow", " 次"))
        self.spinBox_7.setPrefix(_translate("mainWindow", "训练次数：           "))
        self.spinBox_8.setSuffix(_translate("mainWindow", " "))
        self.spinBox_8.setPrefix(_translate("mainWindow", "保留top模型数：   "))
        self.label_6.setText(_translate("mainWindow", "选择模型保存目录"))
        self.pushButton_7.setText(_translate("mainWindow", "开始训练"))
        self.progressBar.setVisible(False)
        self.pushButton_8.setText(_translate("mainWindow", "选择模型导入"))
        self.pushButton_9.setText(_translate("mainWindow", "重置"))
        self.label_8.setText(_translate("mainWindow", "选择掩码 tif 文件"))
        self.pushButton_12.setText(_translate("mainWindow", "预测出图"))
        self.label_10.setText(_translate("mainWindow", "选择 tif 保存目录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("mainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "帮助"))
