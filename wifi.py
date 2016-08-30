# -*- coding: utf-8 -*-
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage

from modules.wifiaccess import get_logs, vaciar_tabla
from ui import mainui


class MainWindow(QMainWindow, mainui.Ui_Main):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        file_dir = os.path.dirname(__file__)
        resource_dir = os.path.join(file_dir, 'icons')
        self.red_button = os.path.join(resource_dir, 'red_button.png')
        self.green_button = os.path.join(resource_dir, 'green_button.png')
        self.orange_button = os.path.join(resource_dir, 'orange_button.png')

        self.twifi = self.tableWiFi
        self.twifi.setColumnCount(3)
        self.twifi.setHorizontalHeaderItem(0, QTableWidgetItem("Fecha"))
        self.twifi.setHorizontalHeaderItem(1, QTableWidgetItem("Tipo Acceso"))
        self.twifi.setHorizontalHeaderItem(2, QTableWidgetItem("Usuario"))

        self.twifi.setColumnWidth(0, 130)
        self.twifi.setColumnWidth(1, 150)
        self.twifi.setColumnWidth(2, 185)

        self.btnAccesos.clicked.connect(self.get_wifi_access)

    def get_wifi_access(self):
        vaciar_tabla(self.twifi)
        get_logs(self.twifi)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
