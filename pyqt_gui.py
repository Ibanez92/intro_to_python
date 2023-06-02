import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Example")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("Hello, GUI World!", self)
        label.move(50, 50)

        button = QPushButton("Click Me!", self)
        button.move(100, 100)
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())