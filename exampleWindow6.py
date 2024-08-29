import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class FramelessWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.8)
        self.setGeometry(100, 100, 400, 300)
                
        self.label = QLabel('hello world', self)
        self.label.setStyleSheet("color: red;")
        self.label.setGeometry(10, 10, 200, 50)
        
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()
            self.old_frame = self.frameGeometry()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.resize(self.old_frame.width() + delta.x(), self.old_frame.height() + delta.y())

    def mouseReleaseEvent(self, event):
        self.old_pos = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frameless_window = FramelessWindow()
    frameless_window.show()
    sys.exit(app.exec_())