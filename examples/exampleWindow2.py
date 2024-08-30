import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
import ctypes
from ctypes import wintypes

# Windows API constants
HWND_TOPMOST = -1
HWND_NOTOPMOST = -2
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_SHOWWINDOW = 0x0040

# Load user32.dll
user32 = ctypes.windll.user32

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Timer to check window state periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_window_state)
        self.timer.start(1000)  # Check every second

    def initUI(self):
        self.setWindowTitle('Non-Minimizable Window')
        self.setGeometry(100, 100, 400, 300)

        # Disable minimize button and close button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint & ~Qt.WindowCloseButtonHint)

    def check_window_state(self):
        if self.isMinimized():
            self.showNormal()
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
            user32.SetWindowPos(int(self.winId()), HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW)
            user32.SetWindowPos(int(self.winId()), HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_SHOWWINDOW)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())