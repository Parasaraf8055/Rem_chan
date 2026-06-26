from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt, QTimer


class SpeechBubble(QLabel):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.ToolTip
        )

        self.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid black;
                border-radius: 10px;
                padding: 8px;
                color: black;
                font-size: 12px;
            }
        """)

        self.hide()

    def show_message(self, text, x, y):

        self.setText(text)

        self.adjustSize()

        self.move(x, y)

        self.show()

        QTimer.singleShot(
            3000,
            self.hide
        )