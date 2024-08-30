import sys, win32gui, win32con
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class TpWindow(QWidget):
    def __init__(self, geometry, opa):
        super().__init__()
        self.x = geometry[0]
        self.y = geometry[1]
        self.w = geometry[2]
        self.h = geometry[3]
        
        self.setWindowFlags(Qt.WindowTransparentForInput | Qt.FramelessWindowHint | Qt.Tool)
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
        class_name = win32gui.GetClassName(hwnd)
        return class_name == "Progman" or class_name == "WorkerW"

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
    def __init__(self, geometry, opa, color, fontSize, rate, step):
        super().__init__(geometry, opa)
        self.rate = rate
        self.step = step
        self.xpos = self.width()
        self.label0 = QLabel('湖南师大二附中F2501班', self)
        self.label0.setStyleSheet(f"color: rgb{tuple(color)}; font-size: {fontSize}px; font-family: '微软雅黑'; font-weight: bold")

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.label_mover)
        self.timer1.start(int(1000/self.rate))

    def change_text(self,text):
        self.label0.setText(text)

    def label_mover(self):
        if self.label0.width() <= self.width():
            self.label0.move(int(0.5*(self.width() - self.label0.width())), int(0.5*(self.height() - self.label0.height())))
        else:
            self.label0.move(self.xpos, int(0.5*(self.height() - self.label0.height())))
            self.xpos = self.xpos - self.step if self.xpos > -self.label0.width() else self.width()






class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(500, 200, 300, 100)
        self.setWindowTitle('Main Window')
        
        self.child_window = MessageWindow([0,0,800,90],1,[255,255,0],80,60,4)
        self.child_window.show()
        
        self.toggle_scaleable_button = QPushButton('Toggle lock', self)
        self.toggle_scaleable_button.clicked.connect(self.child_window.toggle_lock)

        self.toggle_topmost_button = QPushButton('Toggle Topmost', self)
        self.toggle_topmost_button.clicked.connect(self.child_window.toggle_topmost)
        
        layout = QVBoxLayout()
        layout.addWidget(self.toggle_scaleable_button)
        layout.addWidget(self.toggle_topmost_button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())