from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Editor:
    text: str
    curX: int
    curY: int
    selection_width: int

    def set_text(self, text: str) -> None:
        self.text = text

    def set_cursor(self, x: int, y: int) -> None:
        self.curX = x
        self.curY = y

    def set_selection_width(self, width: int) -> None:
        self.selection_width = width

    def create_snapshot(self) -> Snapshot:
        return Snapshot(self, self.text, self.curX, self.curY, self.selection_width)


@dataclass
class Snapshot:
    editor: Editor
    text: str
    curX: int
    curY: int
    selection_width: int

    def restore(self):
        self.editor.set_text(self.text)
        self.editor.set_cursor(self.curX, self.curY)
        self.editor.set_selection_width(self.selection_width)


@dataclass
class Command:
    backup: Snapshot = None

    def make_backup(self) -> None:
        self.backup = self.backup.editor.create_snapshot()

    def undo(self) -> None:
        if self.backup is not None:
            self.backup.restore()


class UpdateCommand(Command):
    def execute(self, new_text: str):
        self.make_backup()
        self.backup.editor.set_text(new_text)


"""
Memento pattern is useful when you want to produce snapshot
of object's state to be able to restore a previous state
of the object.
"""


if __name__ == "__main__":
    editor = Editor("hello", 1, 3, 5)
    print(editor)
    snapshot = editor.create_snapshot()
    update = UpdateCommand(snapshot)
    update.execute("world")
    print(editor)
    update.undo()
    print(editor)
