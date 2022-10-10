from dataclasses import dataclass
from typing import List, Protocol


class Graphic(Protocol):
    def move(self, x: int, y: int) -> None:
        ...

    def draw(self) -> None:
        ...


@dataclass
class Dot:
    x: int
    y: int

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(self.__str__())


@dataclass
class CompoundGraphic:
    children: List[Graphic]

    def add(self, c: Graphic) -> None:
        self.children.append(c)

    def remove(self, c: Graphic) -> None:
        self.children.remove(c)

    def move(self, x: int, y: int) -> None:
        for c in self.children:
            c.move(x, y)

    def draw(self) -> None:
        for c in self.children:
            c.draw()


@dataclass
class Circle(Dot):
    radius: int

    def draw(self) -> None:
        print(f"O{self.__str__()}O")


"""
Here, using composition we can create complex data structure
by nesting data one inside another. Here the compound graphic
can be formed by composition of zero or many Graphic content.
"""

if __name__ == "__main__":
    border = Circle(0, 0, 10)
    left_eye = Dot(-5, 1)
    right_eye = Dot(5, 1)
    mouth = Circle(0, -5, 3)
    face = CompoundGraphic(children=[border, left_eye, right_eye, mouth])
    nose = Circle(0, 0, 1)
    face.add(nose)
    face.draw()

    face.move(10, 20)
    print("moved and draw again:")
    face.draw()
