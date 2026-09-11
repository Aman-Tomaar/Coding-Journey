# Import the system module for handling command-line arguments and application lifecycle
import sys

# Import core PyQt5 window, application, radio button, and button group widgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup


# Define the main application window class inheriting from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the parent QMainWindow class

        # Set window geometry: position x=700, y=300, width=500, height=500
        self.setGeometry(700, 300, 500, 500)

        # Create individual QRadioButton widgets for payment options and order fulfillment
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        # Create two separate button groups to logically separate radio button sets
        # (By default, radio buttons in the same window conflict; groups keep them mutually exclusive per group)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        # Call the user interface setup method
        self.initUI()

    def initUI(self):
        # Position and size each radio button vertically down the window
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # Apply global stylesheet styling to all QRadioButtons (font size, family, and padding)
        self.setStyleSheet(
            "QRadioButton{"
            "font-size: 40px;"
            "font-family: Arial;"
            "padding: 10px;"
            "}"
        )

        # Add payment type radio buttons to the first exclusive button group
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        # Add fulfillment type radio buttons to the second exclusive button group
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Connect the 'toggled' signal of every radio button to the shared handler function
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        # Identify which specific radio button triggered the signal
        radio_button = self.sender()

        # Ensure it prints only when a button is newly checked (avoids duplicate trigger on uncheck)
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


# Application execution entry point
if __name__ == "__main__":
    # Initialize the QApplication instance with system arguments
    app = QApplication(sys.argv)

    # Create an instance of our main window
    window = MainWindow()

    # Display the window on the screen
    window.show()

    # Start the PyQt event loop and exit cleanly when closed
    sys.exit(app.exec_())
