from __future__ import annotations
from dataclasses import dataclass
from re import A

from typing import List, Protocol


class Shape(Protocol):
    def move(self, x: int, y: int) -> None:
        ...

    def draw(self) -> None:
        ...

    def accept(self, visitor: Visitor):
        ...


class Visitor(Protocol):
    def visit_dot(dot: Dot) -> None:
        ...

    def visit_circle(circle: Circle) -> None:
        ...

    def visit_rectangle(rectangle: Rectangle) -> None:
        ...

    def visit_compound_shape(compound_shape: CompoundShape) -> None:
        ...


@dataclass
class Dot:
    x: int
    y: int

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(str(self))

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_dot(self)


@dataclass
class Circle:
    x: int
    y: int
    radius: int

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(str(self))

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)


@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(str(self))

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_rectangle(self)


@dataclass
class CompoundShape:
    shapes: List[Shape]

    def move(self, x: int, y: int) -> None:
        for s in self.shapes:
            s.move(x, y)

    def draw(self) -> None:
        for s in self.shapes:
            s.draw()

    def accept(self, visitor: Visitor) -> None:
        for s in self.shapes:
            s.accept(visitor)


class XMLExportVisitor:
    def visit_dot(self, dot: Dot) -> None:
        print(f"<Dot x='{dot.x}' y='{dot.y}'>.</Dot>")

    def visit_circle(self, circle: Circle) -> None:
        print(
            f"<Circle x='{circle.x}' y='{circle.y}' radius='{circle.radius}'>O</Circle>"
        )

    def visit_rectangle(self, rectangle: Rectangle) -> None:
        print(
            f"<Rectangle x='{rectangle.x}' y='{rectangle.y}' width='{rectangle.width}' height='{rectangle.height}'>[]</Rectangle>"
        )

    def visit_compound_shape(self, compound_shape: CompoundShape) -> None:
        print("<CompundShape>")
        print("</CompoundShape>")


if __name__ == "__main__":
    export_visitor = XMLExportVisitor()
    shapes: List[Shape] = [Dot(1, 2), Circle(2, 4, 5), Rectangle(4, 5, 6, 7)]
    for s in shapes:
        s.accept(export_visitor)
