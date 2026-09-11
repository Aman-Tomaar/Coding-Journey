import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Strange GUI")
        self.setGeometry(
            700, 300, 600, 500
        )  # (x, y, width, height) where [x & y] are cordinates if x & y = 0 then it will appare on the top left of the screen
        self.setWindowIcon(QIcon("C:\\Coding\\img.jpg"))


def main():
    app = QApplication(sys.argv)  # argv means arguments
    window = MainWindow()
    window.show()
    sys.exit(
        app.exec_()
    )  # exec_ is execute : waits for user's input and manage clicks, maximise, minimise, exit etc.


if __name__ == "__main__":
    main()
