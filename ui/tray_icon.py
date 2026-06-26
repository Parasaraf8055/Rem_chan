from PyQt6.QtWidgets import (
    QSystemTrayIcon,
    QMenu
)
from ui.settings_window import SettingsWindow
from PyQt6.QtGui import QAction, QIcon
from ui.chat_window import ChatWindow


class RemTrayIcon(QSystemTrayIcon):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent_window = parent

        self.settings_window = (
            SettingsWindow()
        )

        self.chat_window = ChatWindow()

        self.setIcon(
            QIcon(
                "assets/icons/rem_icon.png"
            )
        )

        menu = QMenu()

        open_action = QAction(
            "Open Rem-Chan"
        )

        talk_action = QAction(
            "Talk"
        )

        settings_action = QAction(
            "Settings"
        )

        exit_action = QAction(
            "Exit"
        )

        open_action.triggered.connect(
            self.show_window
        )

        settings_action.triggered.connect(
            self.open_settings
        )

        talk_action.triggered.connect(
            self.open_chat
        )

        exit_action.triggered.connect(
            self.exit_app
        )

        menu.addAction(
            open_action
        )
        menu.addAction(
            talk_action
        )
        menu.addAction(
            settings_action
        )

        menu.addSeparator()

        menu.addAction(
            exit_action
        )

        self.setContextMenu(menu)

    def open_settings(self):

        self.settings_window.show()

    def open_chat(self):

        self.chat_window.show()

        self.chat_window.raise_()

        self.chat_window.activateWindow()

    def show_window(self):

        self.parent_window.show()


    def exit_app(self):

        self.parent_window.real_exit = True

        self.parent_window.close()