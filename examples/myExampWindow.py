import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowTransparentForInput | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.8)
        self.setGeometry(100, 100, 400, 300)
        
        self.label = QLabel('hello world', self)
        self.label.setStyleSheet("color: red; font-size: 40px; font-weight: bold")
        self.label.setGeometry(10, 10, 900, 50)

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
        if flags & Qt.FramelessWindowHint:
            self.setWindowFlags(flags & ~Qt.FramelessWindowHint)
        else:
            self.setWindowFlags(flags | Qt.FramelessWindowHint)
            self.toggle_selectable()
            self.toggle_selectable()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    def toggle_topmost(self):
        flags = self.windowFlags()
        if flags & Qt.WindowStaysOnTopHint:
            self.setWindowFlags(flags & ~Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(flags | Qt.WindowStaysOnTopHint)
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
        
        self.toggle_scaleable_button = QPushButton('Toggle scaleable', self)
        self.toggle_scaleable_button.clicked.connect(self.child_window.toggle_scaleable)

        self.toggle_topmost_button = QPushButton('Toggle Topmost', self)
        self.toggle_topmost_button.clicked.connect(self.child_window.toggle_topmost)
        
        layout = QVBoxLayout()
        layout.addWidget(self.toggle_selectable_button)
        layout.addWidget(self.toggle_scaleable_button)
        layout.addWidget(self.toggle_topmost_button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())