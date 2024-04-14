import sys
from PyQt6.QtWidgets import QApplication
from ui.systemUI import Ui_mainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = Ui_mainWindow()
    ui.show()

    sys.exit(app.exec())
