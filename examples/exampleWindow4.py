import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSlider, QVBoxLayout, QWidget

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口透明度
        self.setWindowOpacity(0.5)

        # 创建按钮和滑块部件
        self.button = QPushButton("调整透明度")
        self.slider = QSlider()

        # 设置滑块范围和初始值
        self.slider.setRange(0, 100)
        self.slider.setValue(50)

        # 将滑块和按钮添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.slider)

        # 创建一个小部件并将布局设置为窗口的中央部件
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 连接按钮点击事件和滑块值改变事件
        self.button.clicked.connect(self.adjustOpacity)
        self.slider.valueChanged.connect(self.adjustOpacity)

    def adjustOpacity(self):
        opacity = self.slider.value() / 100
        self.setWindowOpacity(opacity)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec_())
