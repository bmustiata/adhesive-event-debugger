from typing import List

import mopyx
import oaas

from adhesive_event_debugger.core import ui_thread


@mopyx.model
class Model:
    def __init__(self):
        self.event_generators: List[str] = []
        self.active_events: List[str] = []


instance = Model()

instance.event_generators.append("x1")


@oaas.service("adhesive-events")
class EventGenerators:
    @ui_thread
    @mopyx.action
    def register_event_generator(self, task_id, task_name) -> None:
        instance.event_generators.append(f"{task_id}:{task_name}")

    @ui_thread
    @mopyx.action
    def register_active_event(self, name) -> None:
        instance.active_events.append(name)  # FIXME

    def is_event_active(self, name) -> bool:
        return name in instance.active_events
