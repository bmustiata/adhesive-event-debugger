from typing import List

import mopyx
import oaas

from adhesive_event_debugger.core import ui_thread


class Event:
    def __init__(self,
                 *,
                 event_id: str,
                 task_id: str,
                 task_name: str) -> None:
        self.event_id = event_id
        self.task_id = task_id
        self.task_name = task_name


class EventGenerator:
    def __init__(self,
                 *,
                 task_id: str,
                 task_name: str) -> None:
        self.task_id = task_id
        self.task_name = task_name


@mopyx.model
class Model:
    def __init__(self):
        self.event_generators: List[EventGenerator] = []
        self.active_events: List[Event] = []


instance = Model()


@oaas.service("adhesive-events")
class EventGenerators:
    @ui_thread
    @mopyx.action
    def register_event_generator(self, task_id, task_name) -> None:
        instance.event_generators.append(EventGenerator(
            task_id=task_id,
            task_name=task_name,
        ))

    @ui_thread
    @mopyx.action
    def register_active_event(self, event_id, task_id, task_name) -> None:
        instance.active_events.append(Event(
            event_id=event_id,
            task_id=task_id,
            task_name=task_name,
        ))

    def is_event_active(self, event_id) -> bool:
        for event in instance.active_events:
            if event.event_id == event_id:
                return True

        return False

