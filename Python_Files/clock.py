import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt6.QtCore import QTimer, QTime, Qt

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Clock")
        self.setGeometry(600, 400, 300, 100)
        self.setStyleSheet("background-color : matte;")
        self.time_label = QLabel(self.current_time, self)
        vbox = QVBoxLayout()

        self.time_label.setStyleSheet("color : green;"
                                      "font-size : 60px;")
        vbox.addWidget(self.time_label)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss:ms AP")
        self.time_label.setText(current_time)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec())