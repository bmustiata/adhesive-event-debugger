import mopyx
from PySide2.QtWidgets import QMainWindow

from adhesive_event_debugger import model
from adhesive_event_debugger.core import clear_layout
from adhesive_event_debugger.ui.event_widget import EventWidget
from adhesive_event_debugger.ui.generated.main_window import Ui_MainWindow
from adhesive_event_debugger.ui.task_widget import TaskWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.add_items()

    def add_items(self):
        self.add_event_generators()
        self.add_active_events()

    @mopyx.render
    def add_event_generators(self):
        clear_layout(self.messages_group_box)
        for event_generator in model.instance.event_generators:
            self.messages_group_box.addWidget(EventWidget(event_generator))

        self.messages_group_box.invalidate()

    @mopyx.render
    def add_active_events(self):
        clear_layout(self.running_group_box)
        for active_event in model.instance.active_events:
            self.running_group_box.addWidget(TaskWidget(active_event))
