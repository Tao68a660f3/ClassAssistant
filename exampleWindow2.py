import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口透明
        self.setWindowOpacity(1.0)

        # 设置窗口背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")  # 设置背景色为完全透明

        self.setGeometry(100, 100, 400, 300)
        
        self.label = QLabel('Hello, World!', self)
        self.label.setGeometry(10, 10, 200, 50)

class SettingsWindow(QWidget):
    def __init__(self, target_window):
        super().__init__()
        self.target_window = target_window
        
        self.setGeometry(500, 200, 300, 100)
        self.setWindowTitle('Settings')
        
        self.selectable_checkbox = QCheckBox('Selectable', self)
        self.selectable_checkbox.move(0,0)
        self.selectable_checkbox.stateChanged.connect(self.toggleSelectable)
        
        self.moveable_checkbox = QCheckBox('Moveable', self)
        self.moveable_checkbox.move(0,30)
        self.moveable_checkbox.stateChanged.connect(self.toggleMoveable)
        
        self.resizable_checkbox = QCheckBox('Resizable', self)
        self.resizable_checkbox.move(0,60)
        self.resizable_checkbox.stateChanged.connect(self.toggleResizable)
        
    def toggleSelectable(self, state):
        self.target_window.setWindowFlag(Qt.WindowType.FramelessWindowHint, state == Qt.CheckState.Checked)
        self.target_window.show()
        
    def toggleMoveable(self, state):
        self.target_window.setWindowFlag(Qt.WindowType.FramelessWindowHint, state == Qt.CheckState.Checked)
        self.target_window.show()
        
    def toggleResizable(self, state):
        self.target_window.setWindowFlag(Qt.WindowType.FramelessWindowHint, state == Qt.CheckState.Checked)
        self.target_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    setting_window = SettingsWindow(window)
    window.show()
    setting_window.show()
    sys.exit(app.exec_())