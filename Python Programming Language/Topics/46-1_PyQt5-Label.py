import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Inherit all initialization methods from QMainWindow

        # Set the window's position (x=700, y=300) and size (width=500, height=500)
        self.setGeometry(700, 300, 500, 500)

        # Create a QLabel widget with the text "Hello" and attach it to this main window
        label = QLabel("Hello", self)

        # Set the font family to Arial and font size to 40
        label.setFont(QFont("Arial", 40))

        # Position the label at x=0, y=0 with a width of 500 and height of 100
        label.setGeometry(0, 0, 500, 100)

        # Apply CSS-like styles (color, background, bold, italic, underline) to the label
        label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        # Alignment reference options (uncomment any to change text placement):
        # label.setAlignment(Qt.AlignTop)  # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        # label.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
        label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER


def main():
    # Initialize the mandatory QApplication instance, passing command-line arguments
    app = QApplication(sys.argv)

    # Create an instance of our customized main window
    window = MainWindow()

    # Make the window visible on the screen
    window.show()

    # Start the PyQt event loop and ensure clean exit when closed
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
