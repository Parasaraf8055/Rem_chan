from PyQt6.QtWidgets import QLabel, QMenu
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication

from core.animation_manager import AnimationManager
from core.movement_manager import MovementManager
from ui.speech_bubble import SpeechBubble
from core.personality_messages import MESSAGES
from core.friendship_manager import FriendshipManager
from core.petting_messages import PET_MESSAGES
from ui.reminder_popup import ReminderPopup
from ui.tray_icon import RemTrayIcon

from modules.reminders.water import WATER_MESSAGES
from modules.reminders.breaks import BREAK_MESSAGES

import random


class RemWindow(QLabel):

    def __init__(self):
        super().__init__()

        # Window Settings
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

      

        # Reminder System
        self.reminder_timer = QTimer()

        self.reminder_timer.timeout.connect(
            self.show_water_reminder
        )

        self.reminder_timer.start(
            600000
        )

        self.can_pet = True
        # Friendship Manager # petting
        self.friendship_manager = FriendshipManager()
        self.setMouseTracking(True)



        
        self.walk_speed = 1
        # Drag Support
        self.old_pos = None

        # Character Size
        self.scale_factor = 0.30

        self.speech_bubble = SpeechBubble()

        self.message_timer = QTimer()

        self.message_timer.timeout.connect(
            self.show_random_message
        )

        self.message_timer.start(30000)

        self.movement_manager = MovementManager()

        self.direction = 1

        self.move_timer = QTimer()

        self.move_timer.timeout.connect(
            self.move_character
        )

        self.move_timer.start(50)

        # Animation System
        self.animation_manager = AnimationManager()

        self.current_state = "idle"

        self.frames = self.animation_manager.get_animation(
            self.current_state
        )

        self.current_frame = 0
    
        if self.frames:

            first_pixmap = QPixmap(
                self.frames[0]
            )

            first_pixmap = first_pixmap.scaled(
                int(first_pixmap.width() * self.scale_factor),
                int(first_pixmap.height() * self.scale_factor),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.resize(
                first_pixmap.width(),
                first_pixmap.height()
            )

    



        # Animation Timer
        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_animation
        )

        self.timer.start(120)

        # State Change Timer
        self.state_timer = QTimer()

        self.state_timer.timeout.connect(
            self.random_state
        )

        self.state_timer.start(10000)
        self.real_exit = False

        self.tray_icon = RemTrayIcon(
            self
        )

        self.tray_icon.show()

    
    def closeEvent(self, event):

        if not self.real_exit:

            event.ignore()

            self.hide()

        else:

            event.accept()

    def reset_petting(self):

        self.can_pet = True

    def enterEvent(self, event):

            if not self.can_pet:
                return

            self.can_pet = False

            self.friendship_manager.increase()

            message = random.choice(
                PET_MESSAGES
            )

            self.speech_bubble.show_message(
                message,
                self.x(),
                self.y() - 60
            )
            if self.friendship_manager.friendship % 10 == 0:

                self.speech_bubble.show_message(
                    "Our friendship is growing. 💙",
                    self.x(),
                    self.y() - 60
                )

            QTimer.singleShot(
                5000,
                self.reset_petting
            )

    def show_water_reminder(self):

        popup = ReminderPopup(
            random.choice(
                WATER_MESSAGES
            )
        )

        popup.show()

        self.current_popup = popup
    def show_random_message(self):

        message = random.choice(MESSAGES)

        bubble_x = self.x()

        bubble_y = self.y() - 50

        self.speech_bubble.show_message(
            message,
            bubble_x,
            bubble_y
    )
    def update_animation(self):

        if not self.frames:
            return

        frame = self.frames[self.current_frame]

        pixmap = QPixmap(frame)

        pixmap = pixmap.scaled(
            int(pixmap.width() * self.scale_factor),
            int(pixmap.height() * self.scale_factor),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.setPixmap(pixmap)
        

        self.setMask(pixmap.mask())

        self.current_frame += 1

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    

    def move_character(self):

        if self.current_state != "walk":
            return

        screen = (
            QApplication.primaryScreen()
            .availableGeometry()
        )

        new_x = (
            self.x()
            + self.walk_speed
            * self.direction
        )

        if new_x <= 0:

            self.direction = 1

        elif (
            new_x
            + self.width()
            >= screen.width()
        ):

            self.direction = -1

        self.move(
            self.x()
            + self.walk_speed
            * self.direction,
            self.y()
        )

    def random_state(self):

        states = [
            "idle",
            "walk"
        ]

        self.current_state = random.choice(states)

        if self.current_state == "walk":

            self.direction = (
                self.movement_manager
                .get_random_direction()
            )

        self.frames = self.animation_manager.get_animation(
            self.current_state
        )

        self.current_frame = 0

    def mousePressEvent(self, event):

        self.old_pos = event.globalPosition().toPoint()

        if event.button() == Qt.MouseButton.LeftButton:

            self.friendship_manager.increase()

            self.speech_bubble.show_message(
                random.choice(PET_MESSAGES),
                self.x(),
                self.y() - 60
            )

        elif event.button() == Qt.MouseButton.RightButton:

            menu = QMenu()

            talk_action = menu.addAction("Talk")

            settings_action = menu.addAction("Settings")

            exit_action = menu.addAction("Exit")

            action = menu.exec(
                event.globalPosition().toPoint()
            )

            if action == talk_action:

                self.tray_icon.open_chat()

            elif action == settings_action:

                self.tray_icon.open_settings()

            elif action == exit_action:

                self.close()


    def mouseMoveEvent(self, event):

        if self.old_pos:

            delta = (
                event.globalPosition().toPoint()
                - self.old_pos
            )

            self.move(
                self.x() + delta.x(),
                self.y() + delta.y()
            )

            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):

        self.old_pos = None