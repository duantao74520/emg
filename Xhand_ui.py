# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:06:40 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqt_file\untitled_2.ui'
#
# Created: Sat Apr 15 09:51:16 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(object): 
    ser = serial.Serial()
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow") #设置主窗口的名称和大小
        MainWindow.resize(1400, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)#设置第一类 串口设置 在主窗口中
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 141, 311))
        self.groupBox.setObjectName("groupBox")
        
        self.label = QtWidgets.QLabel(self.groupBox) #文字占位符
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 41, 16))
        self.label_5.setObjectName("label_5")
        
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)#下拉窗口
        self.comboBox_4.setGeometry(QtCore.QRect(60, 20, 71, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("你好")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 50, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 110, 71, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 140, 71, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 200, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 41, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(70, 170, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)#接收区
        self.groupBox_2.setGeometry(QtCore.QRect(160, 195, 390, 60))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 365, 45))
        self.textBrowser.setObjectName("textBrowser")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)#发送区
        self.groupBox_3.setGeometry(QtCore.QRect(160, 260, 390, 65))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 15, 241, 45))
        self.textEdit.setObjectName("textEdit")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(260, 15, 60, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(325, 15, 60, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 35, 60, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(325, 35, 60, 23))
        self.pushButton_5.setObjectName("pushButton_5")


        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)#第四类 按键功能类
        self.groupBox_4.setGeometry(QtCore.QRect(580, 10, 295, 260))
        self.groupBox.setObjectName("groupBox_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4) #几个功能按键
        self.pushButton_6.setGeometry(QtCore.QRect(10, 15, 61, 23))#小指
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 45, 61, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 75, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)#食指
        self.pushButton_8.setGeometry(QtCore.QRect(80, 15, 61, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 45, 61, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 75, 61, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)#拇指弯曲
        self.pushButton_10.setGeometry(QtCore.QRect(150, 15, 61, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 45, 61, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 75, 61, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_4)#拇指伸缩
        self.pushButton_12.setGeometry(QtCore.QRect(220, 15, 61, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_13.setGeometry(QtCore.QRect(220, 45, 61, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 75, 61, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_back_mode = QtWidgets.QPushButton(self.groupBox_4) #返回
        self.pushButton_back_mode.setGeometry(QtCore.QRect(10, 105, 61, 23))
        self.pushButton_back_mode.setObjectName("pushButton_back_mode")
        self.pushButton_egm_mode = QtWidgets.QPushButton(self.groupBox_4)#emg模式
        self.pushButton_egm_mode.setGeometry(QtCore.QRect(80, 105, 61, 23))
        self.pushButton_egm_mode.setObjectName("pushButton_egm_mode")

        self.groupBox_emg = QtWidgets.QGroupBox(self.groupBox_4)#emg设定区
        self.groupBox_emg.setGeometry(QtCore.QRect(0, 135, 295, 180))
        self.groupBox.setObjectName("groupBox_emg")
        self.lineEdit_emg1_up = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg1_up.setGeometry(QtCore.QRect(10, 10, 61, 20))
        self.lineEdit_emg1_up.setObjectName("lineEdit_emg1_up")
        self.lineEdit_emg1_down = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg1_down.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.lineEdit_emg1_down.setObjectName("lineEdit_emg1_down")
        self.lineEdit_emg1_weak = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg1_weak.setGeometry(QtCore.QRect(10, 50, 61, 20))
        self.lineEdit_emg1_weak.setObjectName("lineEdit_emg1_weak")
        self.pushButton_emg1 = QtWidgets.QPushButton(self.groupBox_emg)
        self.pushButton_emg1.setGeometry(QtCore.QRect(10, 70, 61, 23))
        self.pushButton_emg1.setObjectName("pushButton_emg1")
        self.lineEdit_emg2_up = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg2_up.setGeometry(QtCore.QRect(80, 10, 61, 20))
        self.lineEdit_emg2_up.setObjectName("lineEdit_emg2_up")
        self.lineEdit_emg2_down = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg2_down.setGeometry(QtCore.QRect(80, 30, 61, 20))
        self.lineEdit_emg2_down.setObjectName("lineEdit_emg2_down")
        self.lineEdit_emg2_weak = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg2_weak.setGeometry(QtCore.QRect(80, 50, 61, 20))
        self.lineEdit_emg2_weak.setObjectName("lineEdit_emg2_weak")
        self.pushButton_emg2 = QtWidgets.QPushButton(self.groupBox_emg)
        self.pushButton_emg2.setGeometry(QtCore.QRect(80, 70, 61, 23))
        self.pushButton_emg2.setObjectName("pushButton_emg2")
        self.lineEdit_emg3_up = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg3_up.setGeometry(QtCore.QRect(150, 10, 61, 20))
        self.lineEdit_emg3_up.setObjectName("lineEdit_emg3_up")
        self.lineEdit_emg3_down = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg3_down.setGeometry(QtCore.QRect(150, 30, 61, 20))
        self.lineEdit_emg3_down.setObjectName("lineEdit_emg3_down")
        self.lineEdit_emg3_weak = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg3_weak.setGeometry(QtCore.QRect(150, 50, 61, 20))
        self.lineEdit_emg3_weak.setObjectName("lineEdit_emg3_weak")
        self.pushButton_emg3 = QtWidgets.QPushButton(self.groupBox_emg)
        self.pushButton_emg3.setGeometry(QtCore.QRect(150, 70, 61, 23))
        self.pushButton_emg3.setObjectName("pushButton_emg3")
        self.lineEdit_emg4_up = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg4_up.setGeometry(QtCore.QRect(220, 10, 61, 20))
        self.lineEdit_emg4_up.setObjectName("lineEdit_emg4_up")
        self.lineEdit_emg4_down = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg4_down.setGeometry(QtCore.QRect(220, 30, 61, 20))
        self.lineEdit_emg4_down.setObjectName("lineEdit_emg4_down")
        self.lineEdit_emg4_weak = QtWidgets.QLineEdit(self.groupBox_emg)
        self.lineEdit_emg4_weak.setGeometry(QtCore.QRect(220, 50, 61, 20))
        self.lineEdit_emg4_weak.setObjectName("lineEdit_emg4_weak")
        self.pushButton_emg4 = QtWidgets.QPushButton(self.groupBox_emg)
        self.pushButton_emg4.setGeometry(QtCore.QRect(220, 70, 61, 23))
        self.pushButton_emg4.setObjectName("pushButton_emg4")



        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)#第五类 绘图区
        #self.groupBox_5.setGeometry(QtCore.QRect(580, 180, 295, 140))
        self.groupBox_5.setGeometry(QtCore.QRect(160, 10, 411, 181))
        self.groupBox.setObjectName("groupBox_5")
        self.pyqtgraph1 = GraphicsLayoutWidget(self.groupBox_5)#绘图
        #self.pyqtgraph1.setGeometry(QtCore.QRect(10, 10, 280, 130))
        self.pyqtgraph1.setGeometry(QtCore.QRect(10, 10, 400, 170))
        self.pyqtgraph1.setObjectName("pyqtgraph1")
        self.checkBox_emg=[]
        self.checkBox_emg.append(QtWidgets.QCheckBox(self.groupBox_5))
        self.checkBox_emg[0].setGeometry(QtCore.QRect(350, 10, 20, 20))
        self.checkBox_emg[0].setObjectName("checkBox_emg1")
        self.checkBox_emg.append(QtWidgets.QCheckBox(self.groupBox_5))
        self.checkBox_emg[1].setGeometry(QtCore.QRect(365, 10, 20, 20))
        self.checkBox_emg[1].setObjectName("checkBox_emg2")
        self.checkBox_emg.append(QtWidgets.QCheckBox(self.groupBox_5))
        self.checkBox_emg[2].setGeometry(QtCore.QRect(380, 10, 20, 20))
        self.checkBox_emg[2].setObjectName("checkBox_emg3")
        self.checkBox_emg.append(QtWidgets.QCheckBox(self.groupBox_5))
        self.checkBox_emg[3].setGeometry(QtCore.QRect(395, 10, 20, 20))
        self.checkBox_emg[3].setObjectName("checkBox_emg4")
        '''
        self.pushButton_upgrade = QtWidgets.QPushButton(self.groupBox_5)#emg模式
        self.pushButton_upgrade.setGeometry(QtCore.QRect(10, 10, 61, 23))
        self.pushButton_upgrade.setObjectName("pushButton_upgrade")
        '''

        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)#第六类 调试区
        #self.groupBox_6.setGeometry(QtCore.QRect(580, 180, 295, 140))
        self.groupBox_6.setGeometry(QtCore.QRect(900, 10, 450, 360))
        self.groupBox.setObjectName("groupBox_6")
        self.pyqtgraph_test=[]
        self.pyqtgraph_test.append(GraphicsLayoutWidget(self.groupBox_6))#设定波形
        self.pyqtgraph_test[0].setGeometry(QtCore.QRect(10, 10, 430, 110))
        self.pyqtgraph_test.append(GraphicsLayoutWidget(self.groupBox_6))#设定波形
        self.pyqtgraph_test[1].setGeometry(QtCore.QRect(10, 125, 430, 110))
        self.pyqtgraph_test.append(GraphicsLayoutWidget(self.groupBox_6))#设定波形
        self.pyqtgraph_test[2].setGeometry(QtCore.QRect(10, 240, 430, 110))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow) #主窗口的属性
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());  
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Xhand调试界面"))
        
        self.groupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.label.setText(_translate("MainWindow", "串 口"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.label_3.setText(_translate("MainWindow", "校验位"))
        self.label_4.setText(_translate("MainWindow", "数据位"))
        self.label_5.setText(_translate("MainWindow", "停止位"))
        self.lineEdit_3.setText(_translate("MainWindow", "38400"))
        self.comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "N"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "E"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "O"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "M"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "S"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "COM10"))
        self.pushButton.setText(_translate("MainWindow", "打开"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.pushButton_3.setText(_translate("MainWindow", "检测串口"))
        self.label_11.setText(_translate("MainWindow", "状 态："))
        self.label_12.setText(_translate("MainWindow", "串口状态"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送区"))
        self.checkBox.setText(_translate("MainWindow", "Hex显示"))
        self.checkBox.setChecked(True)
        self.checkBox_2.setText(_translate("MainWindow", "Hex发送"))
        self.checkBox_2.setChecked(True)
        self.pushButton_4.setText(_translate("MainWindow", "清除"))
        self.pushButton_5.setText(_translate("MainWindow", "发送"))

        
        self.groupBox_4.setTitle(_translate("MainWindow", "按键功能区"))
        self.pushButton_6.setText(_translate("MainWindow", "小指曲"))
        self.pushButton_7.setText(_translate("MainWindow", "小指伸"))
        self.lineEdit_4.setText(_translate("MainWindoe","1800"))
        self.pushButton_8.setText(_translate("MainWindow", "食指曲"))
        self.pushButton_9.setText(_translate("MainWindow", "食指伸"))
        self.lineEdit_5.setText(_translate("MainWindoe","1800"))
        self.pushButton_10.setText(_translate("MainWindow", "拇指曲"))
        self.pushButton_11.setText(_translate("MainWindow", "拇指伸"))
        self.lineEdit_6.setText(_translate("MainWindoe","0600"))
        self.pushButton_12.setText(_translate("MainWindow", "拇指内"))
        self.pushButton_13.setText(_translate("MainWindow", "拇指外"))
        self.lineEdit_7.setText(_translate("MainWindow","0900"))
        self.pushButton_back_mode.setText(_translate("MainWindow","返回"))
        self.pushButton_egm_mode.setText(_translate("MainWindow","肌电模式"))
        self.lineEdit_emg1_up.setText(_translate("MainWindow","140"))
        self.lineEdit_emg1_down.setText(_translate("MainWindow","100"))
        self.lineEdit_emg1_weak.setText(_translate("MainWindow","80"))
        self.pushButton_emg1.setText(_translate("MainWindow","EMG1"))
        self.lineEdit_emg2_up.setText(_translate("MainWindow","150"))
        self.lineEdit_emg2_down.setText(_translate("MainWindow","90"))
        self.lineEdit_emg2_weak.setText(_translate("MainWindow","80"))
        self.pushButton_emg2.setText(_translate("MainWindow","EMG2"))
        self.lineEdit_emg3_up.setText(_translate("MainWindow","200"))
        self.lineEdit_emg3_down.setText(_translate("MainWindow","90"))
        self.lineEdit_emg3_weak.setText(_translate("MainWindow","80"))
        self.pushButton_emg3.setText(_translate("MainWindow","EMG3"))
        self.lineEdit_emg4_up.setText(_translate("MainWindow","250"))
        self.lineEdit_emg4_down.setText(_translate("MainWindow","90"))
        self.lineEdit_emg4_weak.setText(_translate("MainWindow","80"))
        self.pushButton_emg4.setText(_translate("MainWindow","EMG4"))

        self.groupBox_5.setTitle(_translate("MainWindow", "绘图区"))
        self.checkBox_emg[0].setText(_translate("MainWindow", "1"))
        self.checkBox_emg[0].setChecked(True)
        self.checkBox_emg[1].setText(_translate("MainWindow", "2"))
        self.checkBox_emg[1].setChecked(True)
        self.checkBox_emg[2].setText(_translate("MainWindow", "3"))
        self.checkBox_emg[2].setChecked(True)
        self.checkBox_emg[3].setText(_translate("MainWindow", "4"))
        self.checkBox_emg[3].setChecked(True)
        '''
        self.pushButton_upgrade.setText(_translate("MainWindow", "更新"))
        '''

        

    