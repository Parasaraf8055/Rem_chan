from PyQt6.QtWidgets import (
    QWidget,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from core.personality import REM_RESPONSES
from modules.ai.llm import RemBrain

class ChatWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Rem-Chan 💙"
        )

        self.resize(
            500,
            600
        )
        self.brain = RemBrain()
        self.chat_history = QTextEdit()

        self.chat_history.setReadOnly(
            True
        )

        self.input_box = QLineEdit()

        self.send_button = QPushButton(
            "Send"
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self.chat_history
        )

        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(
            self.input_box
        )

        bottom_layout.addWidget(
            self.send_button
        )

        layout.addLayout(
            bottom_layout
        )

        self.setLayout(layout)

        self.send_button.clicked.connect(
            self.send_message
        )

 
        
    def send_message(self):

        message = self.input_box.text().lower()

        if not message:
            return

        self.chat_history.append(
            f"You: {message}"
        )

        response = self.brain.ask(
            message
        )

        self.chat_history.append(
            f"Rem: {response}"
        )

        self.input_box.clear()