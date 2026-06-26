import sys

from PyQt6.QtWidgets import QApplication

from ui.main_window import RemWindow

app = QApplication(sys.argv)

window = RemWindow()

window.show()

sys.exit(app.exec())