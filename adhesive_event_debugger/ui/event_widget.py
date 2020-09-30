from PySide2.QtWidgets import QWidget

from adhesive_event_debugger.ui.generated.event_widget import Ui_Form


class EventWidget(QWidget, Ui_Form):
    def __init__(self, name: str) -> None:
        super(EventWidget, self).__init__()

        self.setupUi(self)
        self.label.setText(name)

        self.send_button.clicked.connect(self.send_clicked)

    def send_clicked(self) -> None:
        print("clicked")
