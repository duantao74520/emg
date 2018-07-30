# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:07:22 2018

@author: Administrator
"""
import binascii
import sys
import threading
import queue
import struct
import numpy as np
import pyqtgraph as pg
import serial
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Xhand_ui import Ui_MainWindow


class MyWindows(QMainWindow,Ui_MainWindow):##同时继承QWidget和Ui_MainWindow
    plot_signal = QtCore.pyqtSignal()
    plot_signal_test= QtCore.pyqtSignal()
    emg=[]
    signal_test = []
    for i in range(4):
        emg.append(queue.Queue())
    for i in range(3):
        signal_test.append(queue.Queue())
        
    def __init__(self):
        
        super(MyWindows,self).__init__()#超级加载
        self.setupUi(self)
        self.pushButton.clicked.connect(self.port_open)
        self.pushButton_2.clicked.connect(self.port_close)
        self.pushButton_3.clicked.connect(self.port_cheak)
        self.pushButton_4.clicked.connect(self.clean_data)
        self.pushButton_5.clicked.connect(self.send_data)
        self.pushButton_6.pressed.connect(lambda: self.grasp_or_loose('01','02') )#小指
        self.pushButton_6.released.connect(lambda: self.grasp_or_loose('01','05') )
        self.pushButton_7.pressed.connect(lambda: self.grasp_or_loose('01','03') )
        self.pushButton_7.released.connect(lambda: self.grasp_or_loose('01','05') )
        self.pushButton_8.pressed.connect(lambda: self.grasp_or_loose('02','02') )#食指
        self.pushButton_8.released.connect(lambda: self.grasp_or_loose('02','05') )       
        self.pushButton_9.pressed.connect(lambda: self.grasp_or_loose('02','03') )
        self.pushButton_9.released.connect(lambda: self.grasp_or_loose('02','05') )
        self.pushButton_10.pressed.connect(lambda: self.grasp_or_loose('03','02') )#拇指
        self.pushButton_10.released.connect(lambda: self.grasp_or_loose('03','05') ) 
        self.pushButton_11.pressed.connect(lambda: self.grasp_or_loose('03','03') )
        self.pushButton_11.released.connect(lambda: self.grasp_or_loose('03','05') )
        self.pushButton_12.pressed.connect(lambda: self.grasp_or_loose('04','03') )
        self.pushButton_12.released.connect(lambda: self.grasp_or_loose('04','05') ) 
        self.pushButton_13.pressed.connect(lambda: self.grasp_or_loose('04','02') )
        self.pushButton_13.released.connect(lambda: self.grasp_or_loose('04','05') ) 
        self.pushButton_back_mode.clicked.connect(lambda: self.grasp_or_loose('01','06'))#返回按钮
        self.pushButton_egm_mode.clicked.connect(lambda: self.grasp_or_loose('01','09'))#emg工作模式

        self.pushButton_emg1.clicked.connect(lambda: self.set_emg_data('01') )#设定emg阈值
        self.pushButton_emg2.clicked.connect(lambda: self.set_emg_data('02') )
        self.pushButton_emg3.clicked.connect(lambda: self.set_emg_data('03') )
        self.pushButton_emg4.clicked.connect(lambda: self.set_emg_data('04') )
        self.p1=self.pyqtgraph1.addPlot(title="肌电信号图")
        self.p1.setRange(xRange=[-100, 0])
        self.p1.setLimits(xMax=0)
        self.curve = []
        self.curve.append(self.p1.plot(pen='r',name='1'))
        self.curve.append(pg.PlotCurveItem(pen=(1),name='2'))
        self.curve.append(pg.PlotCurveItem(pen=(80),name='3'))
        self.curve.append(pg.PlotCurveItem(pen=(160),name='4'))
         #self.p1.addItem(self.curve2)
        self.data1 = np.empty(100)
        self.ptr1 = 0
        self.data=[[],[],[],[]]
        self.ptr=[0,0,0,0]
        self.tmp=[[],[],[],[]]
        for i in range(4):
            self.p1.addItem(self.curve[i])
            self.data[i] = np.empty(100)
            self.ptr[i] = 0


        self.p_test = []
        self.curve_test = []
        self.data_test = []
        self.ptr_test = []
        self.tmp_test = []
        for i in range(3):
            self.p_test.append(self.pyqtgraph_test[i].addPlot())
            self.p_test[i].setRange(xRange=[-100, 0])
            self.p_test[i].setLimits(xMax=0)
            self.curve_test.append(self.p_test[i].plot(pen='r'))
            self.data_test.append(np.empty(100))
            self.ptr_test.append(0)
            self.tmp_test.append(0)




       



        self.plot_signal.connect(self.update)

        
    

    #图形更新显示
    def update(self):
        while(not self.emg[0].empty()):
            for i in range(4):
                self.data[i][self.ptr[i]] = int(self.emg[i].get())
                #print(self.ptr[i])
                self.ptr[i] += 1
                if self.ptr[i] >= self.data[i].shape[0]:
                    self.tmp[i] = self.data[i]
                    self.data[i] = np.empty(self.data[i].shape[0] * 2)
                    self.data[i][:self.tmp[i].shape[0]] = self.tmp[i]
                if(self.checkBox_emg[i].isChecked()):
                    self.curve[i].setData(self.data[i][:self.ptr[i]])
                self.curve[i].setPos(-self.ptr[i], 0)
        while( not self.signal_test[0].empty()):
            for i in range(3):
                self.data_test[i][self.ptr_test[i]] = int(self.signal_test[i].get())
                self.ptr_test[i] +=1
                if self.ptr_test[i] >= self.data_test[i].shape[0]:
                    self.tmp_test[i] = self.data_test[i]
                    self.data_test[i] = np.empty(self.data_test[i].shape[0]*2)
                    self.data_test[i][:self.tmp_test[i].shape[0]] = self.tmp_test[i]
                self.curve_test[i].setData(self.data_test[i][:self.ptr_test[i]])
                self.curve_test[i].setPos(-self.ptr_test[i],0)
            


    #信号发射函数
    def run(self):
        self.plot_signal.emit()

        
        
    def port_open(self):
        self.ser.port = self.comboBox_4.currentText()
        self.ser.baudrate = int(self.lineEdit_3.text())
        self.ser.bytesize = int(self.comboBox.currentText()) 
        self.ser.stopbits = int(self.comboBox_3.currentText())
        self.ser.parity = self.comboBox_2.currentText()
        self.ser.open()
        if(self.ser.isOpen()):
            self.pushButton.setEnabled(False)
            self.label_12.setText("打开成功")
            self.t1 = threading.Thread(target=self.receive_data)#d多线程
            self.t1.setDaemon(True)
            self.t1.start() #开始运行
        else:
            self.label_12.setText("打开失败")

    def port_close(self):
        self.ser.close()
        if(self.ser.isOpen()):
            self.label_12.setText("关闭失败")
        else:
            self.pushButton.setEnabled(True)
            self.label_12.setText("关闭成功")


    def send_data(self):
        if(self.ser.isOpen()):
            if(self.checkBox_2.isChecked()):
                 self.ser.write(binascii.a2b_hex(self.textEdit.toPlainText()))
            else:
                self.ser.write(self.textEdit.toPlainText().encode('utf-8'))
            self.label_12.setText("发送成功")
    #       self.ser.flushOutput()
            print(self.textEdit.toPlainText())
        else:
            self.label_12.setText("发送失败")

    def receive_data(self):
        print("The receive_data threading is start")
        res_data = '' 
        res_data_2= []
        num = 0
        while (self.ser.isOpen()): 
            size = self.ser.inWaiting()#检查队列中有多少个在排队
            if size:
                
                res_data = self.ser.read_all() #每次都读取队列中的所有数
                if(self.checkBox.isChecked()):
                    self.textBrowser.append(binascii.b2a_hex(res_data).decode())
                    print(binascii.b2a_hex(res_data).decode()[0:2])
                    if(binascii.b2a_hex(res_data).decode()[0:2] == 'ab'):
                       for i in range (int(len(binascii.b2a_hex(res_data).decode())/20)):
                            self.emg[0].put(res_data[1]+res_data[2]*256)
                            self.emg[1].put(res_data[3]+res_data[4]*256)
                            self.emg[2].put(res_data[5]+res_data[6]*256)
                            self.emg[3].put(res_data[7]+res_data[8]*256)
                            self.run()
                    if(binascii.b2a_hex(res_data).decode()[0:2] == 'ac'):
                        self.signal_test[0].put(struct.unpack('f',res_data[1:5])[0])
                        self.signal_test[1].put(struct.unpack('f',res_data[5:9])[0])
                        self.signal_test[2].put(struct.unpack('f',res_data[9:13])[0]*10000)
                        #print(struct.unpack('f',res_data[9:13])[0]*10000)
                        self.run()

                else:
                    self.textBrowser.append(res_data.decode())
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                self.ser.flushInput()               
                num +=1
                self.label_12.setText("接收："+str(num))

    def clean_data(self):
        self.textBrowser.setText("")
        self.label_12.setText("接收清空")

    def port_cheak(self):
        Com_List=[]
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_4.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboBox_4.addItem(port[0])
        if(len(Com_List) == 0):
            self.label_12.setText("没串口")

    def little_thumb_grasp(self):#小指弯曲
        if(self.ser.isOpen()):
            self.ser.write(binascii.a2b_hex("AA01"+self.lineEdit_4.text()[0:4]+"55"))     
            self.label_12.setText('小指弯曲')
            print('小指弯曲')
        else:
            self.label_12.setText("发送失败")
    def little_thumb_loose(self):#小指伸展
        if(self.ser.isOpen()):
            self.ser.write(binascii.a2b_hex("AA01"+self.lineEdit_4.text()[0:4]+"55"))     
            self.label_12.setText('小指伸展')
            print('小指伸展')
        else:
            self.label_12.setText("发送失败")
    def grasp_or_loose(self,M_Numb,Move_Mode):#手指运动
        if(self.ser.isOpen()):
            
            if(M_Numb == '01' and Move_Mode == '02'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_4.text()[0:4]+"55"))
                self.label_12.setText('小指弯曲')
            elif (M_Numb == '01' and Move_Mode == '03'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_4.text()[0:4]+"55"))
                self.label_12.setText('小指伸展')
            elif(M_Numb == '02'and  Move_Mode == '02'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_5.text()[0:4]+"55"))
                self.label_12.setText('食指弯曲')
            elif (M_Numb == '02' and Move_Mode == '03'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_5.text()[0:4]+"55"))
                self.label_12.setText('食指伸展')
            elif(M_Numb == '03'and Move_Mode == '02'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_6.text()[0:4]+"55"))
                self.label_12.setText('拇指弯曲')
            elif (M_Numb == '03' and Move_Mode == '03'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_6.text()[0:4]+"55"))
                self.label_12.setText('拇指伸展')
            elif(M_Numb == '04'and Move_Mode == '03'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_7.text()[0:4]+"55"))
                self.label_12.setText('拇指内摆')
            elif (M_Numb == '04' and Move_Mode == '02'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_7.text()[0:4]+"55"))
                self.label_12.setText('拇指外摆')
            if (Move_Mode == '05'):
                self.ser.write(binascii.a2b_hex("AA"+M_Numb+Move_Mode+self.lineEdit_7.text()[0:4]+"55"))
                self.label_12.setText('运动停止')
            if(Move_Mode == '06'):
                self.ser.write(binascii.a2b_hex('AA'+M_Numb+Move_Mode+"55"))
                self.label_12.setText('返回运动')
            if(Move_Mode == '09'):
                self.ser.write(binascii.a2b_hex('AA'+M_Numb+Move_Mode+"55"))
                self.label_12.setText('肌电控制模式')
        else:
            self.label_12.setText("发送失败")

    def set_emg_data(self,EMG_num):#EMG阈值设定
        if(self.ser.isOpen()):
            
            if(EMG_num == '01'):  
                self.ser.write(binascii.a2b_hex("AA"+EMG_num+'0B')+struct.pack('b',int(self.lineEdit_emg1_up.text()))+struct.pack('b',int(self.lineEdit_emg1_down.text()))+struct.pack('b',int(self.lineEdit_emg1_weak.text()))+binascii.a2b_hex("55"))
                print(struct.pack('b',int(self.lineEdit_emg1_up.text()))+struct.pack('b',int(self.lineEdit_emg1_down.text()))+struct.pack('b',int(self.lineEdit_emg1_weak.text())))
                self.label_12.setText('EMG1')
            if(EMG_num == '02'):  
                self.ser.write(binascii.a2b_hex("AA"+EMG_num+'0B')+struct.pack('b',int(self.lineEdit_emg2_up.text()))+struct.pack('b',int(self.lineEdit_emg2_down.text()))+struct.pack('b',int(self.lineEdit_emg2_weak.text()))+binascii.a2b_hex("55"))
                print(struct.pack('b',int(self.lineEdit_emg2_up.text()))+struct.pack('b',int(self.lineEdit_emg2_down.text()))+struct.pack('b',int(self.lineEdit_emg2_weak.text())))
                self.label_12.setText('EMG2')
            if(EMG_num == '03'):  
                self.ser.write(binascii.a2b_hex("AA"+EMG_num+'0B')+struct.pack('b',int(self.lineEdit_emg3_up.text()))+struct.pack('b',int(self.lineEdit_emg3_down.text()))+struct.pack('b',int(self.lineEdit_emg3_weak.text()))+binascii.a2b_hex("55"))
                print(struct.pack('b',int(self.lineEdit_emg3_up.text()))+struct.pack('b',int(self.lineEdit_emg3_down.text()))+struct.pack('b',int(self.lineEdit_emg3_weak.text())))
                self.label_12.setText('EMG3')
            if(EMG_num == '04'):  
                self.ser.write(binascii.a2b_hex("AA"+EMG_num+'0B')+struct.pack('b',int(self.lineEdit_emg4_up.text()))+struct.pack('b',int(self.lineEdit_emg4_down.text()))+struct.pack('b',int(self.lineEdit_emg4_weak.text()))+binascii.a2b_hex("55"))
                print(struct.pack('b',int(self.lineEdit_emg4_up.text()))+struct.pack('b',int(self.lineEdit_emg4_down.text()))+struct.pack('b',int(self.lineEdit_emg4_weak.text())))
                self.label_12.setText('EMG4')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindows()
    myWindow.show()
    sys.exit(app.exec_())
   
    '''
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 


    MainWindow.show()
    sys.exit(app.exec_())  
    '''    
