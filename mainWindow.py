import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from settingUI import *

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

    def exitProgram(self):
        # Add any cleanup code here before exiting
        QApplication.instance().quit()

    def initUI(self):
        self.setWindowTitle("设置")

    

    def showMainWindow(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def save_settings(self):
        pass

    def read_settings(self):
        pass
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SettingWindow()
    sys.exit(app.exec_())