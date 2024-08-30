import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class TransparentMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)

        # 设置窗口透明
        self.setWindowOpacity(0.5)

        # 设置窗口背景透明
        self.setStyleSheet("background: transparent;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentMainWindow()
    window.show()
    sys.exit(app.exec_())
