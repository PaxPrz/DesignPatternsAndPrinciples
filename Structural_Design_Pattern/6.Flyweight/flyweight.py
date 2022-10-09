from __future__ import annotations
from functools import partial
from hashlib import md5
from dataclasses import dataclass, field
import random
from colorama import Fore
from typing import List, Set


class Canvas:
    def draw(
        self, type: str, x: int, y: int, name: str, color: str, texture: str
    ) -> None:
        print(f"{color}{type}: [{x}, {y}] {name} ({texture})")


@dataclass
class TreeType:
    name: str
    color: str
    texture: str

    def draw(self, canvas: Canvas, x: int, y: int) -> None:
        canvas.draw("tree", x, y, self.name, self.color, self.texture)

    def __hash__(self) -> str:
        return int(
            md5(f"{self.name} - {self.color} - {self.texture}".encode()).hexdigest(),
            base=16,
        )


class TreeFactory:
    tree_types: Set[TreeType] = set()

    @classmethod
    def get_tree_type(
        cls: TreeFactory, name: str, color: str, texture: str
    ) -> TreeType:
        for t in cls.tree_types:
            if hash(t) == hash(
                int(md5(f"{name} - {color} - {texture}".encode()).hexdigest(), base=16)
            ):
                return t

    @classmethod
    def add_tree_type(cls: TreeFactory, name: str, color: str, texture: str) -> None:
        cls.tree_types.add(TreeType(name, color, texture))


@dataclass
class Tree:
    x: int
    y: int
    type: TreeType

    def draw(self, canvas: Canvas) -> None:
        self.type.draw(canvas, self.x, self.y)


@dataclass
class Forest:
    trees: List[Tree] = field(default_factory=list)

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> Tree:
        type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, type)
        self.trees.append(tree)
        return tree

    def draw(self, canvas: Canvas):
        for t in self.trees:
            t.draw(canvas)


"""
Using this Flyweight pattern, the common attributes are reused
by the system. Those attributes whose value does not change
once initialized can be used as flyweight and reused in another
objects. Here TreeType is a flyweight as the name, color and texture
of a particular tree is same and do not need to be stored in multiple
RAM location.
"""


if __name__ == "__main__":
    r = partial(random.randint, a=0, b=100)
    canvas = Canvas()
    types = [
        ("banayan", Fore.GREEN, "b-b-b"),
        ("mango", Fore.YELLOW, "m-m-m"),
        ("apple", Fore.RED, "a-a-a"),
    ]
    for type in types:
        TreeFactory.add_tree_type(*type)
    forest = Forest()
    for i in range(10):
        tree = forest.plant_tree(r(), r(), *types[i % 3])
    forest.draw(canvas)
