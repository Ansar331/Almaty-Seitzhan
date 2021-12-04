from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Нолики'
                            '')
        self.should_paint_circle = False
        self.lolo = QtWidgets.QPushButton('НАЖАТЬ', self)
        self.lolo.setGeometry(10, 10, 200, 100)
        self.colors = ['RED', 'BLUE', 'GREEN', 'YELLOW']
        self.lolo.clicked.connect(self.paintcircle)
        self.lolo.clicked.connect(self.paintEvent)
        self.should_paint_circle = False

    def paintEvent(self, event):
        if self.should_paint_circle:
            painter = QtGui.QPainter(self)
            painter.setBrush(QColor(self.colors[random.randint(0, 3)]))
            pen = QtGui.QPen()
            pen.setWidth(5)
            painter.setPen(pen)
            a = random.randint(1, 450)
            painter.drawEllipse(130, 130, a, a)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()

