from PySide2.QtWidgets import QMainWindow

from adhesive_event_debugger.ui.generated.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setupUi(self)

