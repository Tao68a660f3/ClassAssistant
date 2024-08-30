import sys
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import datetime

from settingUI import *
from settings import *

class SettingWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.setWindowFlag(Qt.Tool)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('smileface.jpg'))
        self.tray_icon.show()

        self.tray_menu = QMenu()
        show_action = QAction("显示界面", self)
        show_action.triggered.connect(self.show)
        self.tray_menu.addAction(show_action)

        exit_action = QAction("退出程序", self)
        exit_action.triggered.connect(self.exitProgram)
        self.tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.showMainWindow)

        self.settings = setting_dict

    def exitProgram(self):
        # Add any cleanup code here before exiting
        QApplication.instance().quit()

    def initUI(self):
        self.setWindowTitle("设置")
        self.mSize.setMinimum(10)
        self.mSize.setMaximum(256)
        self.mSize.setValue(28)
        self.mSize.setMinimum(10)
        self.mSize.setMaximum(256)
        self.mSize.setValue(28)
        self.sSize.setMinimum(10)
        self.sSize.setMaximum(256)
        self.sSize.setValue(18)
        self.bSize.setMinimum(10)
        self.bSize.setMaximum(256)
        self.bSize.setValue(36)
        self.rate.setMinimum(10)
        self.rate.setMaximum(60)
        self.rate.setValue(30)
        self.step.setMinimum(1)
        self.step.setMaximum(10)
        self.step.setValue(2)

    def read_settings(self):
        pass


    def save_settings(self):
        pass

    def fill_in_set(self):
        self.areaName.setText(self.settings["areaName"])
        self.sayingEdit.setText(self.settings["sayingText"])
        self.noticeOnly.setChecked(self.settings["noticeOnly"])
        self.noticeEdit.setText(self.settings["noticeText"])
        self.checkBox.setChecked(self.settings["autoDatetime"])

        dttm = self.settings["setDatetime"]
        dateTime = QDateTime.currentDateTime()
        dateTime.setDate(QDate(dttm[0], dttm[1], dttm[2]))
        dateTime.setTime(QTime(dttm[3], dttm[4]))
        self.dateTimeEdit.setDateTime(dateTime)

        self.eatalarm.setChecked(self.settings["eatAlarm"])
        
        lchtime = self.settings["lunchTime"]
        dnrtime = self.settings["dinnerTime"]
        self.lunchTime.setTime(QTime(lchtime[0],lchtime[1]))
        self.dinnerTime.setTime(QTime(dnrtime[0],dnrtime[1]))

        ppttim = self.settings["pptOpentime"]
        shuttim = self.settings["shutdownTime"]
        self.pptTime.setTime(QTime(ppttim[0],ppttim[1]))
        self.shutdownTime.setTime(QTime(shuttim[0],shuttim[1]))

        self.mTopMost.setChecked(self.settings["mTopMost"])
        self.sTopMost.setChecked(self.settings["sTopMost"])
        self.bTopMost.setChecked(self.settings["bTopMost"])

        mcolor = (self.settings["messageColor"][0], self.settings["messageColor"][1], self.settings["messageColor"][2])
        scolor = (self.settings["stimeColor"][0], self.settings["stimeColor"][1], self.settings["stimeColor"][2])
        bcolor = (self.settings["btimeColor"][0], self.settings["btimeColor"][1], self.settings["btimeColor"][2])
        self.mColor.setStyleSheet(f"background-color: rgb{mcolor}")
        self.sColor.setStyleSheet(f"background-color: rgb{scolor}")
        self.bColor.setStyleSheet(f"background-color: rgb{bcolor}")

        self.mSize.setValue(self.settings["messageFontsize"])
        self.sSize.setValue(self.settings["stimeFontsize"])
        self.bSize.setValue(self.settings["btimeFontsize"])

        self.mTransp.setRange(0, 100)
        self.sTransp.setRange(0, 100)
        self.bTransp.setRange(0, 100)
        self.mTransp.setValue(100-self.settings["messageTransp"]*100)
        self.sTransp.setValue(100-self.settings["stimeTransp"]*100)
        self.bTransp.setValue(100-self.settings["btimeTransp"]*100)

        self.cnFont.setText(self.settings["cnFont"])
        self.ascFont.setText(self.settings["ascFont"])

        self.rate.setValue(self.settings["flushRate"])
        self.step.setValue(self.settings["step"])





    def showMainWindow(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isHidden():
                self.show()
            else:
                self.hide()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SettingWindow()
    widget.fill_in_set()
    sys.exit(app.exec_())