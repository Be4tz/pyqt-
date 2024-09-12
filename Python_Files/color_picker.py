import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, QGraphicsGridLayout, QPushButton, QLineEdit, QColorDialog)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QFont, QPixmap, QColor

# Background Color Picker App
class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.question = QLabel("Do you want to choose a color for the background?")
        self.but = QPushButton("Yes")
        self.butt = QPushButton("No")
        self.setStyleSheet("""
QPushButton{
                           border-radius : 1px;
                           border : 2px solid black;
                           }

                           
""")
        h = QHBoxLayout()
        v = QVBoxLayout()
        h.addWidget(self.but)
        h.addWidget(self.butt)
        v.addWidget(self.question)
        v.addLayout(h)
        v.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(v)
        self.but.clicked.connect(self.but1)
        self.butt.clicked.connect(self.butt2)
    def but1(self):
        self.question.hide()
        self.but.hide()
        self.butt.hide()
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color : {color.name()}")
        self.question.show()
        self.but.show()
        self.butt.show()
    def butt2(self):
        qurry = """
        Please this the only function of the
        of the app if you know you don't
        want to use it please exit the app"""
        self.question.setText(f"{qurry}")
        self.question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.but.hide()
        self.butt.hide()
        timer = QTimer()
        timer.singleShot(9000, self.afterbutt2)
    def afterbutt2(self):
        self.question.setText("Do you want to choose a color for the background?")
        self.but.show()
        self.butt.show()


def main():
    app = QApplication(sys.argv)
    window = ColorPicker()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
