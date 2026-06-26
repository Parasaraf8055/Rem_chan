from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Rem Settings"
        )

        layout = QVBoxLayout()

        layout.addWidget(
            QLabel(
                "Settings Coming Soon 💙"
            )
        )

        self.setLayout(layout)

        self.resize(
            300,
            200
        )