from __future__ import annotations
from functools import partial
from random import randint
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Protocol


class Prototype(Protocol):
    def clone(self) -> Prototype:
        ...


@dataclass(init=False)
class Shape(ABC):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @abstractmethod
    def clone(self) -> Shape:
        raise NotImplementedError


@dataclass
class Rectangle(Shape):
    width: int
    height: int

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y)
        self.width = width
        self.height = height

    def clone(self) -> Rectangle:
        return Rectangle(self.x, self.y, self.width, self.height)


@dataclass
class Circle(Shape):
    radius: int

    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y)
        self.radius = radius

    def clone(self) -> Circle:
        return Circle(self.x, self.y, self.radius)


"""
For a large and complicated initialization required for an class,
this pattern can be implemented. This will simplify the creation
as it creates object by cloning and existing object. The required
class implements the Prototype class that implements the clone
method.
"""


if __name__ == "__main__":
    r = partial(randint, a=0, b=10)
    shapes: List[Shape] = [
        Rectangle(r(), r(), r(), r()),
        Circle(r(), r(), r()),
        Rectangle(r(), r(), r(), r()),
    ]
    shapes_clone = []
    for s in shapes:
        shapes_clone.append(s.clone())
    print(shapes_clone)
