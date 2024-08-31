import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QTimer

class ShutdownDialog(QWidget):
    def __init__(self):
        super().__init__()

    def show_dlg(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.shutdown)
        self.timer.start(1000)  # 10 seconds
        reply = QMessageBox.question(self, '关机确认', '是否要关机？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.No:
            self.timer.stop()

    def shutdown(self):
        # 在这里编写关机的代码，例如调用系统命令关机
        print("关机")
        self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ShutdownDialog()
    sys.exit(app.exec_())