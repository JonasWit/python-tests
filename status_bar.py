from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QStatusBar
import sys
from PySide2.QtGui import QIcon, QPixmap


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window")
        self.setGeometry(300, 300, 300, 300)

        self.setIcon()
        self.createStatusBar()

    def setIcon(self):
        appIcon = QIcon("logo.png")
        self.setWindowIcon(appIcon)

    def createStatusBar(self):
        self.myStatus = QStatusBar()
        self.myStatus.showMessage("Ready", 3000)
        self.setStatusBar(self.myStatus)


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()
