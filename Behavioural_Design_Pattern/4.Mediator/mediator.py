from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Component:
    dialog: Mediator

    def click(self):
        self.dialog.notify(self, "click")

    def keypress(self, key: str):
        self.dialog.notify(self, "keypress", key=key)


class Button(Component):
    pass


class Textbox(Component):
    text: str = ""

    def get(self) -> str:
        return self.text


class Checkbox(Component):
    checked: bool = False

    def click(self):
        self.check()
        super().click()

    def check(self):
        self.checked = not self.checked


class Mediator(Protocol):
    def notify(self, sender: Component, event: str, **kwargs):
        ...


@dataclass
class AuthenticationDialog:
    title: str = None
    login_or_register: Checkbox = None
    login_username: Textbox = None
    login_password: Textbox = None
    reg_username: Textbox = None
    reg_password: Textbox = None
    reg_email: Textbox = None
    ok: Button = None
    cancel: Button = None
    remember_me: Checkbox = None

    def notify(self, sender: Component, event: str):
        if sender == self.login_or_register and event == "click":
            if self.login_or_register.checked:
                self.title = "Log In"
            else:
                self.title = "Register"
            print("PAGE:", self.title)

        if sender == self.ok and event == "click":
            if self.login_or_register.checked:
                username = self.login_username.get()
                password = self.login_password.get()
                return login(username, password)
            else:
                username = self.reg_username.get()
                password = self.reg_password.get()
                email = self.reg_email.get()
                return register(username, password, email)


def login(username: str, password: str) -> bool:
    print(f"Logging in with {username=} and {password=}")
    return True


def register(username: str, password: str, email: str) -> bool:
    print(f"Registering with {username=}, {password=}, {email=}")
    return True


"""
In Mediator pattern, all the action of component is handled by
the mediator object. Here AuthenticationDialog contains all the
components and acts as mediator. A change in any of its component
will trigger notify in the mediator object.
"""


if __name__ == "__main__":
    mediator = AuthenticationDialog()
    login_or_register_chkbx = Checkbox(mediator)
    login_username_textbox = Textbox(mediator)
    login_password_textbox = Textbox(mediator)
    reg_username_textbox = Textbox(mediator)
    reg_password_textbox = Textbox(mediator)
    reg_email_textbox = Textbox(mediator)
    ok_button = Button(mediator)
    cancel_button = Button(mediator)
    remember_me_chkbx = Checkbox(mediator)
    mediator.login_or_register = login_or_register_chkbx
    mediator.login_username = login_username_textbox
    mediator.login_password = login_password_textbox
    mediator.reg_username = reg_username_textbox
    mediator.reg_password = reg_password_textbox
    mediator.reg_email = reg_email_textbox
    mediator.ok = ok_button
    mediator.cancel = cancel_button
    mediator.remember_me = remember_me_chkbx

    login_or_register_chkbx.click()
    login_username_textbox.text = "ram@email.com"
    login_password_textbox.text = "password"
    ok_button.click()
