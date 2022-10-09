from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Protocol


class ComponentWithContextualHelp(Protocol):
    def show_help(self) -> str:
        ...


@dataclass
class Component:
    container: Container = None
    tooltip_text: str = None

    def show_help(self):
        if self.tooltip_text:
            return self.tooltip_text
        else:
            return self.container.show_help()


@dataclass
class Container(Component):
    children: List[Component] = field(default_factory=list)

    def add(self, child: Component):
        self.children.append(child)


@dataclass
class Panel(Container):
    model_help_text: str = "Panel Help text"

    def show_help(self) -> str:
        return f"Panel: {self.model_help_text}"


@dataclass
class Dialog(Container):
    wiki_page_url: str = "Wiki URL page"

    def show_help(self) -> str:
        return f"Dialog: {self.wiki_page_url}"


@dataclass
class Button(Component):
    pass


"""
In Chain of Responsibility, the responsibility is serially
transferred to next component. Here in this example, a Panel
have multiple dialogs. In a dialog, there are multiple buttons.
If some button do not have help text, then the respective parent
component (Dialog) help is shown. If the Dialog also do not have
help text, the Panel is given the responsibility. In this chain,
if any one of the component can perform the action. The response
returns from there.
"""


if __name__ == "__main__":
    panel = Panel(tooltip_text="panel tooltip", model_help_text="panel help text")
    dialog = Dialog(container=panel, wiki_page_url="my dialog box")
    panel.add(dialog)
    button = Button(container=dialog, tooltip_text="Button tooltip")
    cancel_button = Button(container=dialog)
    dialog.add(button)
    dialog.add(cancel_button)
    print("Button Help:", button.show_help())
    print("Cancel Button Help:", cancel_button.show_help())
    print("Panel Help:", panel.show_help())
