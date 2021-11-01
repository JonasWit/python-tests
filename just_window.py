from PySide2.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget
import sys
from PySide2.QtGui import QIcon, QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test window")
        self.setGeometry(300, 300, 300, 300)


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()
