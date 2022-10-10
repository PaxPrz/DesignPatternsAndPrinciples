from dataclasses import dataclass
from typing import Protocol


class Device(Protocol):
    def is_enabled(self):
        ...

    def enable(self):
        ...

    def disable(self):
        ...

    def get_volume(self) -> int:
        ...

    def set_volume(self, percentage: int) -> None:
        ...

    def get_channel(self) -> int:
        ...

    def set_channel(self, number: int) -> None:
        ...


@dataclass
class Radio:
    company: str
    frequency: float = 100.0
    volume: int = 10
    is_on: bool = False

    def is_enabled(self):
        return self.is_on

    def enable(self):
        self.is_on = True

    def disable(self):
        self.is_on = False

    def get_volume(self) -> int:
        return self.volume

    def set_volume(self, percentage: int) -> None:
        self.volume = percentage

    def get_channel(self) -> int:
        self.frequency

    def set_channel(self, number: int) -> None:
        self.frequency = number


@dataclass
class TV:
    company: str
    channel: int = 1
    volume: int = 20
    is_on: bool = False

    def is_enabled(self):
        return self.is_on

    def enable(self):
        self.is_on = True

    def disable(self):
        self.is_on = False

    def get_volume(self) -> int:
        return self.volume

    def set_volume(self, percentage: int) -> None:
        self.volume = percentage

    def get_channel(self) -> int:
        return self.channel

    def set_channel(self, number: int) -> None:
        self.channel = number


@dataclass
class Remote:
    device: Device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 1)

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)


class AdvancedRemote(Remote):
    def mute(self):
        self.device.set_volume(0)


"""
This pattern seems similar to that of adapter pattern. 
It varies as the pattern works on large number of closely
related classes. In this given example, Radio and TV are
closely related classes.
"""


if __name__ == "__main__":
    tv = TV("Samsung")
    remote = Remote(tv)
    remote.toggle_power()

    radio = Radio("Mi")
    adv_remote = AdvancedRemote(radio)
    adv_remote.toggle_power()
