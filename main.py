import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.flag = False
        # Обратите внимание: имя элемента такое же как в QTDesigner
    def run(self):
        self.flag = True
        self.update()
    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        if self.flag:
            qp.begin(self)
        self.flag = False
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью

        for i in range(random.randint(1, 20)):
            h = random.randint(10, 500)
            qp.drawEllipse(random.randint(10, 800), random.randint(10, 800), h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())