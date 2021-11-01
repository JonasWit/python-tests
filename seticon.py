from PySide2.QtWidgets import QApplication, QWidget
import sys
from PySide2.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings Icon")
        self.setGeometry(300, 300, 300, 300)

        self.setIcon()

    def setIcon(self):
        appIcon = QIcon("logo.png")
        self.setWindowIcon(appIcon)


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()
