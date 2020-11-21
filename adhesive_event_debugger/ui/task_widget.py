import mopyx
from PySide2.QtWidgets import QWidget

from adhesive_event_debugger.model import instance
from adhesive_event_debugger.ui.generated.task_widget import Ui_Form


class TaskWidget(QWidget, Ui_Form):
    def __init__(self, *, event_id, task_name) -> None:
        super(TaskWidget, self).__init__()

        self.event_id = event_id

        self.setupUi(self)

        self.label.setText(task_name)
        self.release_button.clicked.connect(self.release_button_clicked)

    @mopyx.action
    def release_button_clicked(self):
        for index in range(len(instance.active_events)):
            if instance.active_events[index].event_id == self.event_id:
                break

        instance.active_events.pop(index)
