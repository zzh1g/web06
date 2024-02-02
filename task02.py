import os
import sys

import requests
from PyQt5.QtCore import Qt
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown:
            self.spn_ = str(float(self.spn_) / 2)
            self.show_image_()
        elif event.key() == Qt.Key_PageUp:
            self.spn_ = str(float(self.spn_) * 2)
            self.show_image_()

    def show_image_(self):
        longitude = self.longitude.text()
        lattitude = self.lattitude.text()
        self.spn_ = self.spn.text()
        type_maps = self.type_maps.currentText()
        picture = getImage(','.join((longitude, lattitude)), ','.join((self.spn_, self.spn_)), type_maps)
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
