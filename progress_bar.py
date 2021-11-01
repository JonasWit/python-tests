from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QProgressBar, QStatusBar, QPushButton
import sys
from PySide2.QtGui import QIcon, QPixmap
from state import AppState


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window")
        self.setGeometry(300, 300, 300, 300)

        self.statusLabel = QLabel("Progress")
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)

        self.setIcon()
        self.createStatusBar()
        self.setActionButton()

    def setActionButton(self):
        btn2 = QPushButton("Action", self)
        btn2.move(150, 100)
        btn2.clicked.connect(self.buttonAction)

    def setIcon(self):
        appIcon = QIcon("logo.png")
        self.setWindowIcon(appIcon)

    def createStatusBar(self):
        self.statusBar = QStatusBar()
        self.progressBar.setValue(10)
        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.statusBar)

    def buttonAction(self):
        app_state.counter += 1
        self.progressBar.setValue(app_state.counter)


app_state = AppState()
app_state.state = "Initial state"

myapp = QApplication(sys.argv)
window = Window()
window.show()

myapp.exec_()
sys.exit()
