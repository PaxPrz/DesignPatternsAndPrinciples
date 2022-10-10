from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Protocol


class EventListeners(Protocol):
    def update(self, data: Dict[str, str]) -> None:
        ...


class EmailAlertsListener:
    def update(self, data: Dict[str, str]) -> None:
        print(f"Sending email for {data.get('filename')}")


class LoggingListener:
    def update(self, data: Dict[str, str]) -> None:
        print(f"Logging for {data.get('filename')}")


@dataclass
class EventManager:
    listeners: Dict[str, List[EventListeners]] = field(default_factory=dict)

    def subscribe(self, event_type: str, listener: EventListeners) -> None:
        if not event_type in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: EventListeners) -> None:
        self.listeners[event_type].remove(listener)

    def notify(self, event_type: str, data: Dict[str, str]) -> None:
        for listener in self.listeners.get(event_type, []):
            listener.update(data)


@dataclass
class Editor:
    event_manager: EventManager = field(default_factory=EventManager)

    def open_file(self, filename: str):
        """Opens a file"""
        self.event_manager.notify("open", {"filename": filename})

    def save_file(self, filename: str):
        """Saves a file"""
        self.event_manager.notify("save", {"filename": filename})


"""
Observer pattern is one of my favourite design patterns.
This pattern can be used from small to large projects.
Reactions that are dependent on action on another domain
can be added as listeners to particular event. Whenever that
particular event occurs, the event_manager will trigger all
the listeners. This works by pushing (triggering) the listener
to perform reaction.
"""


if __name__ == "__main__":
    email_listener = EmailAlertsListener()
    logging_listener = LoggingListener()

    editor = Editor()
    editor.open_file("ignore.txt")

    editor.event_manager.subscribe("open", logging_listener)
    editor.event_manager.subscribe("save", logging_listener)
    editor.event_manager.subscribe("save", email_listener)

    editor.open_file("BothListener.txt")
    editor.save_file("Emailonly.txt")
