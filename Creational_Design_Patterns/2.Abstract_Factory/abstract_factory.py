from dataclasses import dataclass
from typing import Protocol


class Chair(Protocol):
    def has_legs(self) -> bool:
        ...

    def sit_on(self) -> None:
        ...


@dataclass
class VictorianChair:
    occupied: bool = False

    def has_legs(self) -> bool:
        return True

    def sit_on(self) -> None:
        if self.occupied:
            raise ValueError("Already someone one the chair")
        self.occupied = True


@dataclass
class ModernChair:
    occupied: bool = False

    def has_legs(self) -> bool:
        return False

    def sit_on(self) -> None:
        self.occupied = True


class Sofa(Protocol):
    def sit_count(self) -> int:
        ...


@dataclass
class VictorianSofa:
    def sit_count(self):
        return 4


@dataclass
class ModernSofa:
    def sit_count(self):
        return 3


class FurnitureFactory(Protocol):
    def make_chair(self):
        ...

    def make_sofa(self):
        ...


class VictorianFurnitureFactory:
    def make_chair(self):
        return VictorianChair()

    def make_sofa(self):
        return VictorianSofa()


class ModernFurnitureFactory:
    def make_chair(self):
        return ModernChair()

    def make_sofa(self):
        return ModernSofa()


if __name__ == "__main__":
    choices = ["Victorian", "Modern"]
    choice = input(f"Choose between ({'/'.join(choices)}): ").lower()
    if choice == "victorian":
        app: FurnitureFactory = VictorianFurnitureFactory()
    elif choice == "modern":
        app: FurnitureFactory = ModernFurnitureFactory()
    else:
        raise ValueError("Unknown choice")
    sofa_set = [app.make_chair(), app.make_sofa(), app.make_chair()]
    print(sofa_set)
