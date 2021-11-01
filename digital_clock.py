from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber
import sys
from PySide2.QtCore import QTime, QTimer, SIGNAL
from PySide2.QtGui import QIcon


class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        self.connect(timer, SIGNAL('timeout()'), self.showTime)
        timer.start(1000)
        self.showTime()
        self.setWindowTitle("Timer")
        self.resize(300, 200)

        self.setIcon()

    def setIcon(self):
        appIcon = QIcon("logo.png")
        self.setWindowIcon(appIcon)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if(time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


myapp = QApplication(sys.argv)
window = DigitalClock()
window.show()

myapp.exec_()
sys.exit()
