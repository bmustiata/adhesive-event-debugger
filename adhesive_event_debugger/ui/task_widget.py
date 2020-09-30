from PySide2.QtWidgets import QWidget

from adhesive_event_debugger.ui.generated.task_widget import Ui_Form


class TaskWidget(QWidget, Ui_Form):
    def __init__(self, name: str) -> None:
        super(TaskWidget, self).__init__()

        self.setupUi(self)

