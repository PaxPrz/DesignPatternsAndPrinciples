from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Type


@dataclass
class Command(ABC):
    app: Application
    editor: Editor
    backup: str = None

    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    @abstractmethod
    def execute(self) -> bool:
        """returns if command need to be stored in history"""
        raise NotImplementedError


@dataclass
class CopyCommand(Command):
    def execute(self):
        self.app.clipboard = self.editor.get_selection()
        return False


@dataclass
class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True


@dataclass
class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True


@dataclass
class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return False


@dataclass
class CommandHistory:
    history: List[Command] = field(default_factory=list)

    def push(self, command: Command):
        self.history.append(command)

    def pop(self) -> Command:
        return self.history.pop()


@dataclass
class Editor:
    text: str = ""

    def get_selection(self) -> str:
        return self.text

    def delete_selection(self):
        self.text = ""

    def replace_selection(self, text: str):
        self.text = text


@dataclass
class Application:
    clipboard: str = None
    editors: List[Editor] = field(default_factory=list)
    active_editor: Editor = None
    history: CommandHistory = field(default_factory=CommandHistory)

    def create_UI(self):
        pass

    def execute_command(self, command_class: Type[Command]):
        command = command_class(self, self.active_editor, backup=self.clipboard)
        if command.execute():
            self.history.push(command)

    def undo(self):
        command = self.history.pop()
        if command != None:
            command.undo()

    def set_active_editor(self, editor: Editor):
        self.active_editor = editor


"""
Command Pattern is useful for queueing operations, scheduling
their executeion or execute them remotely. They also provides
reversible operations.
"""


if __name__ == "__main__":
    app = Application()
    editor1 = Editor()
    editor2 = Editor("Something new")
    print("Editor1:", editor1)
    print("Editor2:", editor2)
    app.set_active_editor(editor2)
    app.execute_command(CutCommand)
    print("Cut Editor2")
    print("Editor1:", editor1)
    print("Editor2:", editor2)
    app.set_active_editor(editor1)
    app.execute_command(PasteCommand)
    print("Paste Editor1")
    print("Editor1:", editor1)
    print("Editor2:", editor2)
    app.execute_command(UndoCommand)
    print("Undo")
    print("Editor1:", editor1)
    print("Editor2:", editor2)
    app.execute_command(UndoCommand)
    print("Undo")
    print("Editor1:", editor1)
    print("Editor2:", editor2)
