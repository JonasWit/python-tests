from PySide2.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings Icon")
        self.setGeometry(300, 300, 300, 300)

        self.center()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()
