import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create 5 labels to test with
        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        # Give them background colors so we can see them move around
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # ==========================================
        # 1. VERTICAL LAYOUT (Stacks widgets top-to-bottom)
        # ==========================================
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # central_widget.setLayout(vbox)

        # ==========================================
        # 2. HORIZONTAL LAYOUT (Places widgets side-by-side)
        # ==========================================
        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # central_widget.setLayout(hbox)

        # ==========================================
        # 3. GRID LAYOUT (Places widgets in a row/column grid)
        # ==========================================
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)  # Row 0, Col 0
        grid.addWidget(label2, 0, 1)  # Row 0, Col 1
        grid.addWidget(label3, 1, 0)  # Row 1, Col 0
        grid.addWidget(label4, 1, 1)  # Row 1, Col 1
        grid.addWidget(label5, 1, 2)  # Row 1, Col 2
        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
