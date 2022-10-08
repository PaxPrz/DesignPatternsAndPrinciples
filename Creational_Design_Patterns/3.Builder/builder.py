from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Protocol


@dataclass
class Hall:
    doors: List[str] = field(default_factory=list)
    windows: List[str] = field(default_factory=list)
    walls: List[str] = field(default_factory=list)
    roof: str = None


@dataclass
class Garage:
    gate: str = None
    walls: List[str] = field(default_factory=list)
    roof: str = None


class HouseBuilder(Protocol):
    def reset(self):
        ...

    def build_walls(self, directions: List[str]) -> HouseBuilder:
        ...

    def build_doors(self, directions: List[str]) -> HouseBuilder:
        ...

    def build_windows(self, directions: List[str]) -> HouseBuilder:
        ...

    def build_roof(self, type: str) -> HouseBuilder:
        ...

    def build_gate(self, direction: str) -> HouseBuilder:
        ...

    def get_result(self):
        ...


@dataclass
class HallBuilder:
    _result: Hall = Hall()

    def reset(self):
        self._result = Hall()
        return self

    def build_walls(self, directions: List[str]):
        self._result.walls.extend(directions)
        return self

    def build_doors(self, directions: List[str]):
        self._result.doors.extend(directions)
        return self

    def build_windows(self, directions: List[str]):
        self._result.windows.extend(directions)
        return self

    def build_roof(self, type: str):
        self._result.roof = type
        return self

    def build_gate(self, direction: str):
        print("No gate in Hall")
        return self

    def get_result(self):
        return self._result


@dataclass
class GarageBuilder:
    _result: Garage = Garage()

    def reset(self):
        self._result = Garage()
        return self

    def build_walls(self, directions: List[str]):
        self._result.walls.extend(directions)
        return self

    def build_doors(self, directions: List[str]):
        print("No door in garage")
        return self

    def build_windows(self, directions: List[str]):
        print("No window in garage")
        return self

    def build_roof(self, type: str):
        self._result.roof = type
        return self

    def build_gate(self, direction: str):
        self._result.gate = direction
        return self

    def get_result(self):
        return self._result


@dataclass(init=False)
class Director:
    builder: HouseBuilder

    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def change_builder(self, builder: HouseBuilder):
        self.builder = builder

    def make(self, type: str):
        if type == "old":
            result = self.builder.build_walls(
                ["east", "west", "south"]
            ).build_windows(
                ["south"]
            ).build_doors(
                ["north"]
            ).build_gate(
                "north"
            ).build_roof(
                "chappri"
            ).get_result()
        else:
            result = self.builder.build_walls(
                ["east", "west"],
            ).build_windows(
                ["south", "west"],
            ).build_doors(
                ["east"]
            ).build_gate(
                "north",
            ).build_roof(
                "tile"
            ).get_result()
        return result


'''
According to this pattern, the creation of an class is assigned
to a builder class. The builder has different methods according
to which the instance can have different property after it's creation
gets completed. Here HouseBuilder is implemented by
HallBuilder and GarageBuilder. And accordingly build the respective
object of Hall or Garage with its properties.
Additionally, we can have a Director class, that store the base
rules for creating object with specific properties.
'''


if __name__ == "__main__":
    house_choices = ["garage", "hall"]
    house_choice = input(f"Choose House type ({'/'.join(house_choices)}): ")
    if house_choice == "garage":
        builder = GarageBuilder()
    elif house_choice == "hall":
        builder = HallBuilder()
    else:
        raise ValueError("Invalid Choice")
    choices = ["old", "new"]
    choice = input(f"Choose between ({'/'.join(choices)}) style: ").lower()
    director = Director(builder)
    result = director.make(choice)
    print(result)

