import oaas
from PySide2.QtWidgets import QWidget

from adhesive_event_debugger.ui.generated.event_widget import Ui_Form


@oaas.client("adhesive-process")
class AdhesiveProcess:
    def generate_event(self, task_id: str) -> None:
        ...


class EventGeneratorWidget(QWidget, Ui_Form):
    def __init__(self, *, task_id: str, task_name: str) -> None:
        super(EventGeneratorWidget, self).__init__()

        self.task_id = task_id

        self.setupUi(self)
        self.label.setText(task_name)

        self.send_button.clicked.connect(self.send_clicked)

    def send_clicked(self) -> None:
        oaas.get_client(AdhesiveProcess).generate_event(self.task_id)
