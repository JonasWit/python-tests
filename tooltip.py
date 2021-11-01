from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip
import sys
from PySide2.QtGui import QIcon, QPixmap, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings Icon")
        self.setGeometry(300, 300, 300, 300)

        QToolTip.setFont(QFont("Decorative", 10, QFont.Bold))
        self.setToolTip("Our Main Window")

        self.setIcon()
        self.setIconModes()

    def setIcon(self):
        appIcon = QIcon("logo.png")
        self.setWindowIcon(appIcon)

    def setIconModes(self):
        icon1 = QIcon("logo.png")
        label1 = QLabel('Sample', self)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)
        label1.setToolTip("Active Icon")

        icon2 = QIcon("logo.png")
        label2 = QLabel("sample", self)
        pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100, 0)
        label1.setToolTip("Disabled Icon")

        icon3 = QIcon("logo.png")
        label3 = QLabel("sample", self)
        pixmap3 = icon3.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(100, 100)
        label3.setToolTip("Selected Icon")


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()
