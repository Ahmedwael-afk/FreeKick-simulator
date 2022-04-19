# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_8 = QtWidgets.QWidget(self.widget_7)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalSlider_Dist = QtWidgets.QSlider(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_Dist.sizePolicy().hasHeightForWidth())
        self.verticalSlider_Dist.setSizePolicy(sizePolicy)
        self.verticalSlider_Dist.setMinimum(1)
        self.verticalSlider_Dist.setMaximum(110)
        self.verticalSlider_Dist.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Dist.setObjectName("verticalSlider_Dist")
        self.horizontalLayout_6.addWidget(self.verticalSlider_Dist)
        self.Label_Distance = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Distance.sizePolicy().hasHeightForWidth())
        self.Label_Distance.setSizePolicy(sizePolicy)
        self.Label_Distance.setObjectName("Label_Distance")
        self.horizontalLayout_6.addWidget(self.Label_Distance)
        self.verticalSlider_Theta = QtWidgets.QSlider(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_Theta.sizePolicy().hasHeightForWidth())
        self.verticalSlider_Theta.setSizePolicy(sizePolicy)
        self.verticalSlider_Theta.setMinimum(-30)
        self.verticalSlider_Theta.setMaximum(30)
        self.verticalSlider_Theta.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Theta.setObjectName("verticalSlider_Theta")
        self.horizontalLayout_6.addWidget(self.verticalSlider_Theta)
        self.Label_Theta = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Theta.sizePolicy().hasHeightForWidth())
        self.Label_Theta.setSizePolicy(sizePolicy)
        self.Label_Theta.setObjectName("Label_Theta")
        self.horizontalLayout_6.addWidget(self.Label_Theta)
        self.horizontalLayout_4.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget_7)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.ball_up = QtWidgets.QLabel(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ball_up.sizePolicy().hasHeightForWidth())
        self.ball_up.setSizePolicy(sizePolicy)
        self.ball_up.setText("")
        self.ball_up.setScaledContents(True)
        self.ball_up.setObjectName("ball_up")
        self.horizontalLayout_5.addWidget(self.ball_up)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_7)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalSlider_V_int = QtWidgets.QSlider(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_V_int.sizePolicy().hasHeightForWidth())
        self.verticalSlider_V_int.setSizePolicy(sizePolicy)
        self.verticalSlider_V_int.setMinimum(1)
        self.verticalSlider_V_int.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_V_int.setObjectName("verticalSlider_V_int")
        self.horizontalLayout_7.addWidget(self.verticalSlider_V_int)
        self.Label_V_initial = QtWidgets.QLabel(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_V_initial.sizePolicy().hasHeightForWidth())
        self.Label_V_initial.setSizePolicy(sizePolicy)
        self.Label_V_initial.setObjectName("Label_V_initial")
        self.horizontalLayout_7.addWidget(self.Label_V_initial)
        self.verticalSlider_Phy = QtWidgets.QSlider(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_Phy.sizePolicy().hasHeightForWidth())
        self.verticalSlider_Phy.setSizePolicy(sizePolicy)
        self.verticalSlider_Phy.setMinimum(0)
        self.verticalSlider_Phy.setMaximum(180)
        self.verticalSlider_Phy.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_Phy.setObjectName("verticalSlider_Phy")
        self.horizontalLayout_7.addWidget(self.verticalSlider_Phy)
        self.Label_Phy = QtWidgets.QLabel(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Phy.sizePolicy().hasHeightForWidth())
        self.Label_Phy.setSizePolicy(sizePolicy)
        self.Label_Phy.setObjectName("Label_Phy")
        self.horizontalLayout_7.addWidget(self.Label_Phy)
        self.horizontalLayout_4.addWidget(self.widget_10)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_14 = QtWidgets.QWidget(self.widget_3)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ball_left = QtWidgets.QLabel(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ball_left.sizePolicy().hasHeightForWidth())
        self.ball_left.setSizePolicy(sizePolicy)
        self.ball_left.setText("")
        self.ball_left.setScaledContents(True)
        self.ball_left.setObjectName("ball_left")
        self.horizontalLayout_9.addWidget(self.ball_left)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.widget_14)
        self.widget_15 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.goal = QtWidgets.QLabel(self.widget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goal.sizePolicy().hasHeightForWidth())
        self.goal.setSizePolicy(sizePolicy)
        self.goal.setText("")
        self.goal.setPixmap(QtGui.QPixmap("Images/Goal.jpg"))
        self.goal.setScaledContents(True)
        self.goal.setObjectName("goal")
        self.verticalLayout_6.addWidget(self.goal)
        self.horizontalLayout_3.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.widget_3)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.ball_right = QtWidgets.QLabel(self.widget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ball_right.sizePolicy().hasHeightForWidth())
        self.ball_right.setSizePolicy(sizePolicy)
        self.ball_right.setText("")
        self.ball_right.setScaledContents(True)
        self.ball_right.setObjectName("ball_right")
        self.horizontalLayout_10.addWidget(self.ball_right)
        self.horizontalLayout_3.addWidget(self.widget_16)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_11 = QtWidgets.QWidget(self.widget_2)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_maxHeight = QtWidgets.QLabel(self.widget_11)
        self.label_maxHeight.setObjectName("label_maxHeight")
        self.verticalLayout.addWidget(self.label_maxHeight)
        self.horizontalLayout_8.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_2)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem5)
        self.pushButton_kick = QtWidgets.QPushButton(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.pushButton_kick.setFont(font)
        self.pushButton_kick.setObjectName("pushButton_kick")
        self.verticalLayout_4.addWidget(self.pushButton_kick)
        self.horizontalLayout_8.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.widget_2)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ballHeight = QtWidgets.QLabel(self.widget_13)
        self.label_ballHeight.setObjectName("label_ballHeight")
        self.verticalLayout_3.addWidget(self.label_ballHeight)
        self.horizontalLayout_8.addWidget(self.widget_13)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.ball_1 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ball_1.sizePolicy().hasHeightForWidth())
        self.ball_1.setSizePolicy(sizePolicy)
        self.ball_1.setText("")
        self.ball_1.setPixmap(QtGui.QPixmap("Images/Football.jpg"))
        self.ball_1.setScaledContents(True)
        self.ball_1.setObjectName("ball_1")
        self.horizontalLayout_2.addWidget(self.ball_1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.horizontalLayout.addWidget(self.widget_6)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Label_Distance.setText(_translate("MainWindow", "Distance"))
        self.Label_Theta.setText(_translate("MainWindow", "Theta"))
        self.Label_V_initial.setText(_translate("MainWindow", "V_initial"))
        self.Label_Phy.setText(_translate("MainWindow", "Phy"))
        self.label_maxHeight.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_kick.setText(_translate("MainWindow", "Kick!!"))
        self.label_ballHeight.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
