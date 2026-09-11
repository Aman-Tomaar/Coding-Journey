import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        # Create a push button with text and attach it to the window
        self.button = QPushButton("Click me!", self)
        self.initUI()

    def initUI(self):
        # Set button position (x=150, y=200) and size (width=200, height=100)
        self.button.setGeometry(150, 200, 200, 100)

        # Style the button font size using CSS-like syntax
        self.button.setStyleSheet("font-size: 30px;")

        # Connect the button's clicked signal to our custom slot/method
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        # This function runs automatically whenever the button is clicked
        print("Button clicked!")


if __name__ == "__main__":  # Fixed single underscores to double underscores
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
