import sys
from PyQt5.QtCore import QTimer, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scheduled Action')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Waiting for scheduled time...', self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Set the specific time for the action
        self.scheduled_time = QTime(10, 43, 0)  # 15:30:00

        # Create a timer to check the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.timer.start(1000)  # Check every second

    def check_time(self):
        current_time = QTime.currentTime()
        if current_time >= self.scheduled_time:
            self.perform_action()
            self.timer.stop()  # Stop the timer after the action is performed

    def perform_action(self):
        self.label.setText('Scheduled action performed!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())