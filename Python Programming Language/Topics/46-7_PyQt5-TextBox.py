# Import system module for managing command-line arguments and application lifecycle
import sys

# Import core PyQt5 widgets for windows, applications, text input boxes, and clickable buttons
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton


# Define the main application window class inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the parent QMainWindow class

        # Set window position (x=700, y=300) and dimensions (width=500, height=500)
        self.setGeometry(700, 300, 500, 500)

        # Create a QLineEdit widget (text input field) attached to this window
        self.line_edit = QLineEdit(self)

        # Create a QPushButton widget labeled "Submit" attached to this window
        self.button = QPushButton("Submit", self)

        # Call the user interface layout and event setup method
        self.initUI()

    def initUI(self):
        # Position and size the text input box (x=10, y=10, width=200, height=40)
        self.line_edit.setGeometry(10, 10, 200, 40)

        # Position and size the submit button next to the input box (x=210, y=10, width=100, height=40)
        self.button.setGeometry(210, 10, 100, 40)

        # Apply CSS-like styling to the text input for font size and family
        self.line_edit.setStyleSheet("font-size: 25px;" "font-family: Arial")

        # Apply identical font styling to the submit button for visual consistency
        self.button.setStyleSheet("font-size: 25px;" "font-family: Arial")

        # Set greyed-out placeholder text inside the input field to guide the user
        self.line_edit.setPlaceholderText("Enter your name")

        # Connect the button's 'clicked' signal to our custom 'submit' handler method
        self.button.clicked.connect(self.submit)

    def submit(self):
        # Retrieve the current text entered into the QLineEdit input field
        text = self.line_edit.text()

        # Print a greeting formatted with the user's input to the console
        print(f"Hello {text}")


# Execution entry point for the script
if __name__ == "__main__":
    # Initialize the core QApplication instance with system arguments
    app = QApplication(sys.argv)

    # Create an instance of our main window
    window = MainWindow()

    # Make the window visible on the screen
    window.show()

    # Start the application event loop and cleanly exit upon closing
    sys.exit(app.exec_())
