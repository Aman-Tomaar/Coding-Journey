# Import system module for handling command-line arguments and application lifecycle
import sys

# Import core PyQt5 widgets and alignment/state constants
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt5.QtCore import Qt


# Define the main application window class inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the parent QMainWindow class

        # Set window position (x=700, y=300) and dimensions (width=500, height=500)
        self.setGeometry(700, 300, 500, 500)

        # Create a QCheckBox widget with a text prompt and attach it to this window
        self.checkbox = QCheckBox("Do you like food?", self)

        # Call the layout and style initialization method
        self.initUI()

    def initUI(self):
        # Set the checkbox's position and size within the window
        self.checkbox.setGeometry(10, 0, 500, 100)

        # Apply CSS-like styling to change the font size and family
        self.checkbox.setStyleSheet("font-size: 30px;" "font-family: Arial;")

        # Connect the checkbox's stateChanged signal to our custom event handler method
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # Check if the current state of the checkbox matches the Qt.Checked constant
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You DO NOT like food")


# Execution entry point for the script
if __name__ == "__main__":
    # Initialize the QApplication instance, passing system arguments
    app = QApplication(sys.argv)

    # Create an instance of our MainWindow class
    window = MainWindow()

    # Render and display the window on the screen
    window.show()

    # Start the application event loop and cleanly exit upon closing
    sys.exit(app.exec_())
