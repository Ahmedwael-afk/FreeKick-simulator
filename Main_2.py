from Gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os
import sys
import time
import math
import threading
import numpy as np
from os import path
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from scipy.stats import norm
from PyQt5.uic import loadUiType


Q = 7.32
S = 2.44
G = 9.8



FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__), "Gui.ui"))
class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self , parent=None):
        super(MainApp,self)._init_(parent)
        QMainWindow._init_(self)
        self.setupUi(self)


        self.ball_1.setPixmap(QtGui.QPixmap("Images/Football.jpg"))
        self.goal.setPixmap(QtGui.QPixmap("Images/Goal.jpg"))
        self.verticalSlider_Dist.valueChanged.connect(self.setDist)
        self.verticalSlider_Phy.valueChanged.connect(self.setPhy)
        self.verticalSlider_Theta.valueChanged.connect(self.setTheta)
        self.verticalSlider_V_int.valueChanged.connect(self.setVelocity)
        self.pushButton_kick.clicked.connect(self.Goal_or_Not)
        # self.ball_1.setPixmap(QtGui.QPixmap("Images/Football.jpg"))
        # self.ball_1.setPixmap(QtGui.QPixmap("Images/Football.jpg"))
        self.player = QMediaPlayer()


    def setDist(self,value_D):
        self.Label_Distance.setText(str(value_D))
        self.value_D = value_D

    def setTheta(self,value_Theta):
        self.Label_Theta.setText(str(value_Theta))
        self.value_Theta = value_Theta

    def setPhy(self,value_Phy):
        self.Label_Phy.setText(str(value_Phy))
        self.value_Phy = value_Phy

    def setVelocity(self,value_V_Int):
        self.Label_V_initial.setText(str(value_V_Int))
        self.value_V_Int = value_V_Int


    def playAudioFile(self):
        url = QUrl.fromLocalFile(self.File_Path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        # currentVolume = self.player.volume() #
        # self.player.setVolume(currentVolume - 30)
        self.player.play()




    def Goal_or_Not(self):


        self.ball_up.clear()
        self.ball_left.clear()
        self.ball_right.clear()
        self.goal.setPixmap(QtGui.QPixmap("Images/GOAL.jpg"))

        d = self.value_D
        input_theta = self.value_Theta                          # Horizontal angle of shooting
        theta = (input_theta * math.pi)/180        # Take the input angle in degrees
        input_phy= self.value_Phy                              # Vertical angle of shooting 
        phy = (input_phy * math.pi)/180
        V_initial = self.value_V_Int                             # The initial velocity of kicking the ball  
        result = "Unable to deduce!"

        if (theta > 0) and (abs(math.tan(theta)) >= (0.5 * Q)/d):    # Check the horizontal angle
            self.ball_left.setPixmap(QtGui.QPixmap("Images/Football.jpg"))
            self.File_Path = os.path.join(os.getcwd(),"Images/missed.mp3")
            self.playAudioFile()

        elif (theta < 0) and (abs(math.tan(theta)) >= (0.5 * Q)/d):
            self.ball_right.setPixmap(QtGui.QPixmap("Images/Football.jpg"))
            self.File_Path = os.path.join(os.getcwd(),"Images/missed.mp3")
            self.playAudioFile()
                

        else:
                                    #### Phase 1 ####
            #V_x_1 = V_initial * acos(phy)
            #V_y_2 = V_initial * asin(phy) - (G * T)

            T = (V_initial * abs(math.sin(phy))) / G                         # Calc time taken to reach highest point at phase 1
            S_x_1 = V_initial * abs(math.cos(phy)) * T                       # Then using time calc horizontal distace covered 
            S_y_1 = (V_initial * abs(math.sin(phy)) * T) - ((G * T * T)/2)   # Then calc the height at this time 
            print("time", T, "height", S_y_1, "dist", S_x_1)
            print("sin(phy)", abs(math.sin(phy)))
            print("phy", phy)
            print("slider phy", self.value_Phy)
                                         #### Phase 2 ####

                      #### we want to know the height of the ball (S_y_2) when it reaches the goal line (S_x_2) ####

            S_x_2 = d - S_x_1
            T_2 = (S_x_2) / (V_initial * abs(math.cos(phy))) 
            S_y_2 = G * T_2 * T_2 * 0.5
            S_y_3 = S_y_1 - S_y_2

            if (S_y_3 >= S) or (S_x_1 > d):
                self.ball_up.setPixmap(QtGui.QPixmap("Images/Football.jpg"))
                self.File_Path = os.path.join(os.getcwd(),"Images/missed.mp3")
                self.playAudioFile()
            else :
                self.goal.setPixmap(QtGui.QPixmap("Images/score.jpg"))
                self.File_Path = os.path.join(os.getcwd(),"Images/scored.mp3")
                self.playAudioFile()

            maxHeight = "Max height is " + str(round(S_y_1,3)) + " after " + str(round(T,3))  + " secs."
            self.label_maxHeight.setText(maxHeight)
            if T_2 >= T:
                ballHeight = "Balls height at goal line is 0 meters."
                self.label_ballHeight.setText(ballHeight)
            else:
                ballHeight = "Balls height at goal line is  " + str(round(S_y_3,3)) + " meters."
                self.label_ballHeight.setText(ballHeight)




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '_main_':
    main()