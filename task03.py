import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget
from api_yandex_maps import getImage
from task_01_ui import Ui_MainWindow


class Example(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.show_image.clicked.connect(self.push)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown:
            self.spn = str(float(self.spn) / 2)
            self.show_image_()
        elif event.key() == Qt.Key_PageUp:
            self.spn = str(float(self.spn) * 2)
            self.show_image_()
        elif event.key() == Qt.Key_Up:
            self.lattitude = str(float(self.lattitude) - float(self.spn) / 4)
            self.show_image_()
        elif event.key() == Qt.Key_Down:
            self.lattitude = str(float(self.lattitude) + float(self.spn) / 4)
            self.show_image_()
        elif event.key() == Qt.Key_Left:
            self.longitude = str(float(self.longitude) + float(self.spn) / 4)
            self.show_image_()
        elif event.key() == Qt.Key_Right:
            self.longitude = str(float(self.longitude) - float(self.spn) / 4)
            self.show_image_()

    def show_image_(self):
        picture = getImage(','.join((self.longitude, self.lattitude)), ','.join((self.spn, self.spn)),
                           self.type_maps)
        self.pixmap = QPixmap.fromImage(QImage.fromData(picture))
        self.image.setPixmap(self.pixmap)
        self.setFocus()

    def push(self):
        self.longitude = self.longitude.text()
        self.lattitude = self.lattitude.text()
        self.spn = self.spn.text()
        self.type_maps = self.type_maps.currentText()
        self.show_image_()

    def initUI(self):
        self.setWindowTitle('Отображение карты')
        self.longitude = self.longitude.text()
        self.lattitude = self.lattitude.text()
        self.spn = self.spn.text()
        self.type_maps = self.type_maps.currentText()
        self.show_image_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
