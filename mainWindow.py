import sys, os, ast
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QAction, QColorDialog
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
        self.ColorChoose = QColorDialog(self)
        self.read_settings()

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

        self.mColor.clicked.connect(lambda: self.get_color("messageColor"))
        self.sColor.clicked.connect(lambda: self.get_color("stimeColor"))
        self.bColor.clicked.connect(lambda: self.get_color("btimeColor"))

        self.exitBtn.clicked.connect(self.save_settings)

    def get_color(self, obj):
        self.ColorChoose.exec_()
        col = self.ColorChoose.selectedColor()
        if col.isValid():
            color = [col.red(), col.green(), col.blue()]
        else:
            color = [255,0,0]
        self.settings[obj] = color
        self.fill_in_set()
        QApplication.processEvents()

    def read_settings(self):
        if os.path.exists("settings"):
            with open("settings", "r", encoding="utf-8") as f:
                self.settings = ast.literal_eval(f.read())
        else:
            self.settings = setting_dict


    def save_settings(self):
        self.settings["areaName"] = self.areaName.text()
        self.settings["sayingText"] = self.sayingEdit.toPlainText().replace("\n"," ")
        self.settings["noticeOnly"] = self.noticeOnly.isChecked()
        self.settings["noticeText"] = self.noticeEdit.toPlainText().replace("\n"," ")
        self.settings["autoDatetime"] = self.checkBox.isChecked()

        dttmget = self.dateTimeEdit.dateTime()
        y = dttmget.date().year()
        m = dttmget.date().month()
        d = dttmget.date().day()
        H = dttmget.time().hour()
        M = dttmget.time().minute()
        self.settings["setDatetime"] = [y,m,d,H,M]

        self.settings["eatAlarm"] = self.eatalarm.isChecked()
        
        lchtime = self.lunchTime.time()
        dnrtime = self.dinnerTime.time()
        self.settings["lunchTime"] = [lchtime.hour(),lchtime.minute()]
        self.settings["dinnerTime"] = [dnrtime.hour(),dnrtime.minute()]

        ppttim = self.pptTime.time()
        shuttim = self.shutdownTime.time()
        self.settings["pptOpentime"] = [ppttim.hour(),ppttim.minute()]
        self.settings["shutdownTime"] = [shuttim.hour(),shuttim.minute()]

        self.settings["mTopMost"] = self.mTopMost.isChecked()
        self.settings["sTopMost"] = self.sTopMost.isChecked()
        self.settings["bTopMost"] = self.bTopMost.isChecked()

        self.settings["mLock"] = self.mLock.isChecked()
        self.settings["sLock"] = self.sLock.isChecked()
        self.settings["bLock"] = self.bLock.isChecked()

        self.settings["messageFontsize"] = self.mSize.value()
        self.settings["stimeFontsize"] = self.sSize.value()
        self.settings["btimeFontsize"] = self.bSize.value()

        self.settings["messageTransp"] = (100-self.mTransp.value())/100
        self.settings["stimeTransp"] = (100-self.sTransp.value())/100
        self.settings["btimeTransp"] = (100-self.bTransp.value())/100

        self.settings["cnFont"] = self.cnFont.text()
        self.settings["ascFont"] = self.ascFont.text()

        self.settings["flushRate"] = self.rate.value()
        self.settings["step"] = self.step.value()

        with open("settings","w",encoding="utf-8") as f:
            f.write(str(self.settings)) 

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

        self.mLock.setChecked(self.settings["mLock"])
        self.sLock.setChecked(self.settings["sLock"])
        self.bLock.setChecked(self.settings["bLock"])

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
        self.mTransp.setValue(int(100-self.settings["messageTransp"]*100))
        self.sTransp.setValue(int(100-self.settings["stimeTransp"]*100))
        self.bTransp.setValue(int(100-self.settings["btimeTransp"]*100))

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