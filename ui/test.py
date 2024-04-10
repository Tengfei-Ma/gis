import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("mainWindow.ui")
    ui.show()

    sys.exit(app.exec())
