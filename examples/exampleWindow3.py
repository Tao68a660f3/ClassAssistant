import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.8)
        self.setGeometry(100, 100, 400, 300)
        
        self.label = QLabel('hello world', self)
        self.label.setStyleSheet("color: red;")
        self.label.setGeometry(10, 10, 200, 50)
        
        self.is_selectable = True
        self.is_topmost = True
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()
            self.old_frame = self.frameGeometry()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.old_frame.topLeft() + delta)

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    def toggle_selectable(self):
        if self.is_selectable:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.is_selectable = not self.is_selectable
        self.show()

    def toggle_topmost(self):
        if self.is_topmost:
            self.setWindowFlags(Qt.FramelessWindowHint)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.is_topmost = not self.is_topmost
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(500, 200, 300, 100)
        self.setWindowTitle('Main Window')
        
        self.child_window = TransparentWindow()
        self.child_window.show()
        
        self.toggle_selectable_button = QPushButton('Toggle Selectable', self)
        self.toggle_selectable_button.clicked.connect(self.child_window.toggle_selectable)
        
        self.toggle_topmost_button = QPushButton('Toggle Topmost', self)
        self.toggle_topmost_button.clicked.connect(self.child_window.toggle_topmost)
        
        layout = QVBoxLayout()
        layout.addWidget(self.toggle_selectable_button)
        layout.addWidget(self.toggle_topmost_button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())