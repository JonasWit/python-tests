from PySide2.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
import sys
from PySide2.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AboutBox Creation")
        self.setGeometry(300, 200, 500, 400)

        self.setIcon()
        self.pushButton()

    def setIcon(self):
        appIcon = QIcon("logo.png")
        self.setWindowIcon(appIcon)

    def pushButton(self):
        self.aboutButtton = QPushButton("Open About Box", self)
        self.aboutButtton.move(50, 100)
        self.aboutButtton.clicked.connect(self.aboutBox)

    def aboutBox(self):
        QMessageBox.about(self.aboutButtton, "About Pyside2",
                          "Pyside2 is a Cross Platform GUI Library For Python Programming Language")


myapp = QApplication(sys.argv)
window = Window()
window.show()


myapp.exec_()
sys.exit()
