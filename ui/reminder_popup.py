from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class ReminderPopup(QWidget):

    def __init__(self, message):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.Tool
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setWindowTitle("Rem-Chan")

        layout = QVBoxLayout()

        label = QLabel(message)

        layout.addWidget(label)

        self.setLayout(layout)

        self.resize(250, 100)