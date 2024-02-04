import os
import sys

import requests
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from api_yandex_maps import getImage
from task_01_ui import Ui_MainWindow


class Example(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.show_image.clicked.connect(self.show_image_)

    def show_image_(self):
        longitude = self.longitude_.text()
        lattitude = self.lattitude_.text()
        spn = self.spn_.text()
        type_maps = self.type_maps_.currentText()
        picture = getImage(','.join((longitude, lattitude)), ','.join((spn, spn)), type_maps)
        self.pixmap = QPixmap.fromImage(QImage.fromData(picture))
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.setWindowTitle('Отображение карты')
        self.show_image_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
