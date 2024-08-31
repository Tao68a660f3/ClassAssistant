import sys, os, ast, shutil, win32gui, win32con
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSystemTrayIcon, QMenu, QAction, QColorDialog, QMessageBox
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

        self.show()

class BigWindow(TpWindow):
    def __init__(self, parent, geometry, opa):
        super().__init__(geometry, opa)
        self.parent = parent
        self.TIMETO = None
        self.TimeDelta = None
        self.text1 = "距%Year%年高考还剩"
        self.text2 = "%d|%H|%m"
        self.text3 = "Day"
        self.text4 = "Hour"
        self.text5 = "Min"
        self.label1 = QLabel(self.text1, self)
        self.label2 = QLabel(self.text2, self)
        self.label3 = QLabel(self.text3, self)
        self.label4 = QLabel(self.text4, self)
        self.label5 = QLabel(self.text5, self)
        self.reset_time()
        self.calculate_deltatime()

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.reset_attr)
        self.timer1.start(1000)

    def calculate_deltatime(self):
        if self.parent.SETTING["autoDatetime"]:
            self.TimeDelta = self.next_gaokao()
        else:
            self.reset_time()
            self.TimeDelta = self.TIMETO - datetime.datetime.now()

    def next_gaokao(self):
        year = datetime.datetime.now().year
        thisGaokao = datetime.datetime(year,6,7,9,0)
        timeDelta = thisGaokao - datetime.datetime.now()
        if timeDelta.days < 0:
            thisGaokao = datetime.datetime(year+1,6,7,9,0)
        timeDelta = thisGaokao - datetime.datetime.now()
        self.TIMETO = thisGaokao
        return timeDelta
    
    def reset_time(self):
        t = self.parent.SETTING["setDatetime"]
        self.TIMETO = datetime.datetime(year = t[0], month = t[1], day = t[2], hour = t[3],minute = t[4],second = 0)

    def reset_attr(self):
        color, fontSize, fontFamily = self.parent.SETTING["btimeColor"], self.parent.SETTING["btimeFontsize"], self.parent.SETTING["ascFont"]
        self.calculate_deltatime()
        start = int(0.5*(self.width()-self.label2.width()))
        width = self.label2.width()
        days = str(self.TimeDelta.days)
        hours = str(self.TimeDelta.seconds//3600)
        mins = str((self.TimeDelta.seconds%3600)//60)
        if len(hours) == 1:
            hours = "0"+hours
        if len(mins) == 1:
            mins = "0"+mins
        leng = len(days)+len(hours)+len(mins)+2
        w = int(width/leng)
        w0 = int(width*len(days)/leng)
        w1 = int(width*len(hours)/leng)
        w2 = int(width*len(mins)/leng)

        self.label1.setText(self.text1.replace("%Year%",str(self.TIMETO.year)))
        self.label1.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {fontSize}px; font-family: {fontFamily}; font-weight: bold")
        self.label1.adjustSize()
        self.label1.move(0,0)

        self.label2.setText(days+"|"+hours+"|"+mins)
        self.label2.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {int(fontSize*2.5)}px; font-family: {fontFamily}; font-weight: bold")
        self.label2.adjustSize()
        self.label2.move(start,self.label1.height()+int(0.5*self.label1.height()))

        self.label3.setText(self.text3)
        self.label3.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {int(fontSize*0.8)}px; font-family: {fontFamily}; font-weight: bold")
        self.label3.adjustSize()
        self.label3.move(start+int(0.5*(w0-self.label3.width())),self.label2.height()+int(1.5*self.label1.height()))

        self.label4.setText(self.text4)
        self.label4.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {int(fontSize*0.8)}px; font-family: {fontFamily}; font-weight: bold")
        self.label4.adjustSize()
        self.label4.move(start+w0+w+int(0.5*(w1-self.label4.width())),self.label2.height()+int(1.5*self.label1.height()))

        self.label5.setText(self.text5)
        self.label5.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {int(fontSize*0.8)}px; font-family: {fontFamily}; font-weight: bold")
        self.label5.adjustSize()
        self.label5.move(start+w0+w1+2*w+int(0.5*(w2-self.label5.width())),self.label2.height()+int(1.5*self.label1.height()))

        self.resize(max(self.label1.width(),self.label2.width()), self.label1.height()+int(2*self.label2.height()))

    # 每一个窗口类都加上这两个事件处理
    def moveEvent(self,event):
        # 在窗口位置改变时执行的操作
        gem = [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
        self.parent.SETTING["btimeGeometry"] = gem

    def resizeEvent(self, event):
        # 在窗口大小改变时执行的操作
        gem = [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
        self.parent.SETTING["btimeGeometry"] = gem

class SmallWindow(TpWindow):
    def __init__(self, parent, geometry, opa):
        super().__init__(geometry, opa)
        self.parent = parent
        self.TIMETO = None
        self.TimeDelta = None
        self.text1 = "距高考还剩%GaoKaoDay%天"
        self.text2 = "%Y/%m/%d %H:%M:%S"
        self.label1 = QLabel(self.text1, self)
        self.label2 = QLabel(self.text2, self)
        self.reset_time()
        self.calculate_deltatime()

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.reset_attr)
        self.timer1.start(1000)

    def calculate_deltatime(self):
        if self.parent.SETTING["autoDatetime"]:
            self.TimeDelta = self.next_gaokao()
        else:
            self.TimeDelta = self.TIMETO - datetime.datetime.now()

    def next_gaokao(self):
        year = datetime.datetime.now().year
        thisGaokao = datetime.datetime(year,6,7,9,0)
        timeDelta = thisGaokao - datetime.datetime.now()
        if timeDelta.days < 0:
            thisGaokao = datetime.datetime(year+1,6,7,9,0)
        timeDelta = thisGaokao - datetime.datetime.now()
        return timeDelta
    
    def reset_time(self):
        t = self.parent.SETTING["setDatetime"]
        self.TIMETO = datetime.datetime(year = t[0], month = t[1], day = t[2], hour = t[3],minute = t[4],second = 0)

    def reset_attr(self):
        color, fontSize, fontFamily = self.parent.SETTING["stimeColor"], self.parent.SETTING["stimeFontsize"], self.parent.SETTING["cnFont"]
        self.calculate_deltatime()

        self.label1.setText(self.text1.replace("%GaoKaoDay%",str(self.TimeDelta.days)))
        self.label1.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {int(fontSize*1.25)}px; font-family: {fontFamily}; font-weight: bold")
        self.label1.adjustSize()
        self.label1.move(int(0.5*(self.width()-self.label1.width())),0)

        self.label2.setText(datetime.datetime.now().strftime(self.text2))
        self.label2.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {fontSize}px; font-family: {fontFamily}; font-weight: bold")
        self.label2.adjustSize()
        self.label2.move(int(0.5*(self.width()-self.label2.width())),self.label1.height()+int(0.5*self.label2.height()))

        self.resize(max(self.label1.width(),self.label2.width()), self.label1.height()+int(1.5*self.label2.height()))

    # 每一个窗口类都加上这两个事件处理
    def moveEvent(self,event):
        # 在窗口位置改变时执行的操作
        gem = [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
        self.parent.SETTING["stimeGeometry"] = gem

    def resizeEvent(self, event):
        # 在窗口大小改变时执行的操作
        gem = [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
        self.parent.SETTING["stimeGeometry"] = gem

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
        
    # 每一个窗口类都加上这两个事件处理
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

class ShutdownDialog(QWidget):
    def __init__(self,parent):
        super().__init__(parent)

    def show_dlg(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.shutdown)
        self.timer.start(15000)  # 10 seconds
        reply = QMessageBox.question(self, '关机确认', '是否要关机？请在15秒内确认！', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.No:
            self.timer.stop()

    def shutdown(self):
        # 在这里编写关机的代码，例如调用系统命令关机
        print("关机")
        os.system("shutdown -s -t 0")
        self.timer.stop()

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
        self.ShutdownDlg = ShutdownDialog(self)
        self.read_settings()

    def exitProgram(self):
        self.parent.keep_run = False
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

        self.OpenPPT.clicked.connect(self.open_ppt)
        self.exitBtn.clicked.connect(self.save_settings)

    def open_ppt(self):
        os.startfile(self.parent.thisPPT)

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
        self.keep_run = True
        self.message = ""
        self.timeDelta = None
        self.thisPPT = None
        self.canteenAccept = False

        self.SettingWindow = SettingWindow(self)
        self.SETTING = self.SettingWindow.settings

        self.create_ppt()

        # 设置目标时间
        ppt_time = self.SETTING["pptOpentime"]
        self.ppt_target_time = datetime.datetime.combine(datetime.date.today(),datetime.time(ppt_time[0], ppt_time[1]))

        shut_time = self.SETTING["shutdownTime"]
        self.shut_target_time = datetime.datetime.combine(datetime.date.today(),datetime.time(shut_time[0], shut_time[1]))

        self.MessageWindow = MessageWindow(self,self.SETTING["messageGeometry"],self.SETTING["messageTransp"],self.SETTING["flushRate"],self.SETTING["step"])
        self.SmallWindow = SmallWindow(self,self.SETTING["stimeGeometry"],self.SETTING["stimeTransp"])
        self.BigWindow = BigWindow(self,self.SETTING["btimeGeometry"],self.SETTING["btimeTransp"])

        self.init_windows()

        self.SettingWindow.mTopMost.clicked.connect(self.MessageWindow.toggle_topmost)
        self.SettingWindow.mLock.clicked.connect(self.MessageWindow.toggle_lock)
        self.SettingWindow.sTopMost.clicked.connect(self.SmallWindow.toggle_topmost)
        self.SettingWindow.sLock.clicked.connect(self.SmallWindow.toggle_lock)
        self.SettingWindow.bTopMost.clicked.connect(self.BigWindow.toggle_topmost)
        self.SettingWindow.bLock.clicked.connect(self.BigWindow.toggle_lock)

        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.check_time)
        self.timer1.start(1500)

    def create_ppt(self):
        dirname = os.path.join("homework",str(datetime.datetime.now().month))
        dirname = os.path.abspath(dirname)
        filename = datetime.datetime.now().strftime("%y%m%d.pptx")
        self.thisPPT = os.path.join(os.path.abspath(dirname),filename)
        print(self.thisPPT)
        print(dirname)

        try:
            os.mkdir("homework")
            os.mkdir(dirname)
            shutil.copy("template.pptx",self.thisPPT)
        except:
            pass        

    def init_windows(self):
        self.MessageWindow.reset_attr(self.SETTING["messageColor"],self.SETTING["messageFontsize"],self.SETTING["cnFont"])
        self.MessageWindow.show()
        self.SmallWindow.show()
        self.BigWindow.show()

    def do_something(self):
        print("Action performed at specific time")

    def open_ppt(self):
        os.startfile(self.thisPPT)

    def check_time(self):
        # 更新目标时间
        ppt_time = self.SETTING["pptOpentime"]
        ppt_target_time_day = self.ppt_target_time.date()
        ppt_target_time_min = datetime.time(ppt_time[0],ppt_time[1])
        self.ppt_target_time = datetime.datetime.combine(ppt_target_time_day,ppt_target_time_min)

        shut_time = self.SETTING["shutdownTime"]
        shut_target_time_day = self.shut_target_time.date()
        shut_target_time_min = datetime.time(shut_time[0],shut_time[1])
        self.shut_target_time = datetime.datetime.combine(shut_target_time_day,shut_target_time_min)

        lunch_time = self.SETTING["lunchTime"]
        dinner_time = self.SETTING["dinnerTime"]
        t_lunch_time = datetime.time(lunch_time[0],lunch_time[1])
        t_dinner_time = datetime.time(dinner_time[0],dinner_time[1])
        t_lunch_time = datetime.datetime.combine(datetime.datetime.today(),t_lunch_time)
        t_dinner_time = datetime.datetime.combine(datetime.datetime.today(),t_dinner_time)

        current_time = datetime.datetime.now()
        
        if current_time >= self.ppt_target_time:
            self.open_ppt()
            self.ppt_target_time = self.ppt_target_time + datetime.timedelta(days=1)

        if current_time >= self.shut_target_time and current_time < self.shut_target_time + datetime.timedelta(seconds=60):
            self.SettingWindow.ShutdownDlg.show_dlg()
            self.shut_target_time = self.shut_target_time + datetime.timedelta(days=1)

        eat = (current_time >= t_lunch_time + datetime.timedelta(seconds= -15) and current_time < t_lunch_time) or (current_time >= t_dinner_time + datetime.timedelta(seconds= -15) and current_time < t_dinner_time)

        if eat and self.SETTING["eatAlarm"]:
            self.MessageWindow.text = "请准备下课用餐"
            self.MessageWindow.reset_attr(self.SETTING["messageColor"],self.SETTING["messageFontsize"],self.SETTING["cnFont"])
            
            if not self.canteenAccept:
                canteen = QMessageBox(self.SettingWindow)
                canteen.setIcon(QMessageBox.Question)
                canteen.setWindowTitle("食堂发来了一个邀请")
                canteen.setText("亲爱的老师，我们可以去吃饭了吗？")
                ok = canteen.addButton('当然可以', QMessageBox.AcceptRole)  # 使用 addButton() 方法添加自定义按钮
                no = canteen.addButton('讲完这个', QMessageBox.RejectRole)
                canteen.setDefaultButton(ok)
                canteen.setWindowFlag(Qt.WindowStaysOnTopHint)
                happy = canteen.exec_()
                if happy == QMessageBox.AcceptRole:
                    self.canteenAccept = True
                self.continueRunning()  # 继续运行程序
        else:
            self.canteenAccept = False

    def continueRunning(self):
        # 阻止主事件循环退出，使程序继续运行
        app.aboutToQuit.connect(self.keepRunning)

    def keepRunning(self):
        # 添加一个循环来保持应用程序运行
        while self.keep_run:
            app.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Run = RunController()
    sys.exit(app.exec_())