import sys, os, ast, win32gui, win32con
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSystemTrayIcon, QMenu, QAction, QColorDialog
from PyQt5.QtGui import QIcon
from getWeather import *
import datetime


from settingUI import *
from settings import *


class TpWindow(QWidget):
    def __init__(self, geometry, opa):
        super().__init__()
        self.x = geometry[0]
        self.y = geometry[1]
        self.w = geometry[2]
        self.h = geometry[3]
        self.setWindowFlags(Qt.Tool)
        flags = self.windowFlags()
        self.setWindowFlags(flags | Qt.WindowTransparentForInput | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(opa)
        self.setGeometry(self.x, self.y, self.w, self.h)

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.check_overlap)
        self.timer1.start(500)

    def toggle_selectable(self):
        flags = self.windowFlags()
        if flags & Qt.WindowTransparentForInput:
            self.setWindowFlags(flags & ~Qt.WindowTransparentForInput)
        else:
            self.setWindowFlags(flags | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    def toggle_scaleable(self):
        flags = self.windowFlags()
        if flags & Qt.WindowMinimizeButtonHint:
            self.setWindowFlags(flags & ~Qt.WindowMinimizeButtonHint)
        else:
            self.setWindowFlags(flags | Qt.WindowMinimizeButtonHint)

        flags = self.windowFlags()
        if flags & Qt.FramelessWindowHint:
            self.setWindowFlags(flags & ~Qt.FramelessWindowHint)
        else:
            self.setWindowFlags(flags | Qt.FramelessWindowHint)
            self.toggle_selectable()
            self.toggle_selectable()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    def toggle_lock(self):
        self.toggle_selectable()
        self.toggle_scaleable()

    def toggle_topmost(self):
        flags = self.windowFlags()
        if flags & Qt.WindowStaysOnTopHint:
            self.setWindowFlags(flags & ~Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(flags | Qt.WindowStaysOnTopHint)
        self.show()

    # 在check_overlap方法中调用bring_window_to_top函数来将本窗口移到桌面上方
    def bring_window_to_top(self,hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def is_desktop_window(self,hwnd):
        try:
            class_name = win32gui.GetClassName(hwnd)
            return class_name == "Progman" or class_name == "WorkerW"
        except:
            return False

    # 在check_overlap方法中调用is_desktop_window函数来确认窗口是否是Windows桌面
    def check_overlap(self):
        hwnd = win32gui.GetForegroundWindow()
        
        if self.is_desktop_window(hwnd):
            # print("This is the Windows desktop.")
            self.bring_window_to_top(self.winId())  # 将本窗口移到桌面上方
            flags = self.windowFlags()
            if flags & Qt.WindowStaysOnTopHint:
                self.setWindowFlags(flags & ~Qt.WindowStaysOnTopHint)


class MessageWindow(TpWindow):
    def __init__(self, parent, geometry, opa, rate, step):
        super().__init__(geometry, opa)
        self.parent = parent
        self.WeatherGet = WeatherGeter(city_data)
        self.WeatherGet.get_area_id(self.parent.SETTING["areaName"])
        self.index = -1
        self.moving = False
        self.rate = rate
        self.step = step
        self.xpos = self.width()
        self.text = "电子倒计时和天气预报工具"
        self.msg = ["","","","","","",]
        self.label0 = QLabel(self.text, self)

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.label_mover)
        self.timer1.start(int(1000/self.rate))

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.get_weather)
        self.timer2.start(300000)

        self.timer3 = QTimer(self)
        self.timer3.timeout.connect(self.msg_update)
        self.timer3.start(30000)

        self.get_weather()

    def reset_attr(self, color, fontSize, fontFamily):
        self.label0.setText(self.text)
        self.label0.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {fontSize}px; font-family: {fontFamily}; font-weight: bold")
        self.label0.adjustSize()

    def get_weather(self):
        today = "今日天气" + self.WeatherGet.get_weather_content("1d")
        sevenday = "本周天气" + self.WeatherGet.get_weather_content("7d")
        self.msg[0] = today if "fail" not in today.lower() else self.msg[0]
        self.msg[1] = sevenday if "fail" not in sevenday.lower() else self.msg[1]

    def msg_update(self):
        self.msg[2] = self.parent.SETTING["noticeText"]
        self.msg[3] = self.parent.SETTING["sayingText"]

        if not self.moving: 
            self.index = self.index + 1 if self.index + 1 < len(self.msg) else 0
            while self.msg[self.index].strip() == "" :
                self.index = self.index + 1 if self.index + 1 < len(self.msg) else 0
            self.text = self.msg[self.index]
            if self.parent.SETTING["noticeOnly"]:
                self.text = self.parent.SETTING["noticeText"]
            self.reset_attr(self.parent.SETTING["messageColor"],self.parent.SETTING["messageFontsize"],self.parent.SETTING["cnFont"])
            self.xpos = self.width()
        # print(self.text)
        
    def moveEvent(self,event):
        # 在窗口位置改变时执行的操作
        gem = [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
        self.parent.SETTING["messageGeometry"] = gem

    def resizeEvent(self, event):
        # 在窗口大小改变时执行的操作
        gem = [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
        self.parent.SETTING["messageGeometry"] = gem

    def label_mover(self):
        if self.label0.width() <= self.width():
            self.moving = False
            self.label0.move(int(0.5*(self.width() - self.label0.width())), int(0.5*(self.height() - self.label0.height())))
            
        else:
            self.moving = True
            self.label0.move(self.xpos, int(0.5*(self.height() - self.label0.height())))
            if self.xpos > -self.label0.width():
                self.xpos = self.xpos - self.step
            else:
                self.xpos = self.width()
                self.moving = False
                self.msg_update()

class SettingWindow(QWidget, Ui_Form):
    def __init__(self,parent):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.setWindowFlag(Qt.Tool)

        self.parent = parent

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
        self.fill_in_set()


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

        self.parent.init_windows()

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
                flags = self.windowFlags()
                if flags & Qt.WindowStaysOnTopHint:
                    self.setWindowFlags(flags & ~Qt.WindowStaysOnTopHint)
                else:
                    self.setWindowFlags(flags | Qt.WindowStaysOnTopHint)
            else:
                self.hide()

class RunController():
    def __init__(self):
        self.message = ""
        self.timeDelta = None

        self.SettingWindow = SettingWindow(self)
        self.SETTING = self.SettingWindow.settings

        self.MessageWindow = MessageWindow(self,self.SETTING["messageGeometry"],self.SETTING["messageTransp"],self.SETTING["flushRate"],self.SETTING["step"])

        self.init_windows()


        self.SettingWindow.mTopMost.clicked.connect(self.MessageWindow.toggle_topmost)
        self.SettingWindow.mLock.clicked.connect(self.MessageWindow.toggle_lock)


        

    def init_windows(self):
        self.MessageWindow.reset_attr(self.SETTING["messageColor"],self.SETTING["messageFontsize"],self.SETTING["cnFont"])
        self.MessageWindow.show()



            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Run = RunController()
    sys.exit(app.exec_())