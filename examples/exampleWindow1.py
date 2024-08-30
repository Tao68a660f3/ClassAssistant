import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Custom Taskbar Example')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowFlag(Qt.Tool)
        self.show()

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('smileface.jpg'))
        self.tray_icon.show()

        self.tray_icon.activated.connect(self.showMainWindow)

    def showMainWindow(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.show()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())