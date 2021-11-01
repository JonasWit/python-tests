from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sys
from state import AppState


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(app_state.state)
        self.setGeometry(300, 300, 300, 300)

        self.setQuitButton()
        self.setActionButton()

    def setQuitButton(self):
        btn1 = QPushButton("Quit", self)
        btn1.move(50, 100)
        btn1.clicked.connect(self.quiteApp)

    def setActionButton(self):
        btn2 = QPushButton("Action", self)
        btn2.move(150, 100)
        btn2.clicked.connect(self.buttonAction)

    def quiteApp(self):
        userInfo = QMessageBox.question(
            self, "Confirmation", "Do you want to Quit?", QMessageBox.Yes | QMessageBox.No)

        if userInfo == QMessageBox.Yes:
            myApp.quit()
        elif userInfo == QMessageBox.No:
            pass

    def buttonAction(self):
        app_state.counter += 1
        app_state.state = f"{app_state.state} - {app_state.counter}"
        print(app_state.counter)


app_state = AppState()
app_state.state = "Initial state"

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)
