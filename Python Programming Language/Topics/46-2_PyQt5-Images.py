import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 400, 400)

        # Use a raw string (r"...") to avoid path escape character issues
        pixmap = QPixmap(r"C:\Coding\img.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        # Center the label inside the main window
        label.setGeometry(
            (self.width() - label.width()) // 2,
            (self.height() - label.height()) // 2,
            label.width(),
            label.height(),
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":  # Fixed single underscores to double underscores
    main()
