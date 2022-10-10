from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class GameAI(ABC):
    def take_turn(self):
        """take turn"""

    def collect_resources(self):
        """collect resources"""

    @abstractmethod
    def build_structures(self):
        raise NotImplementedError

    @abstractmethod
    def build_units(self):
        raise NotImplementedError

    def attack(self):
        """attack"""

    def send_scouts(self, position: Any):
        """send scouts"""

    def send_warriors(self, position: Any):
        """send warriors"""


class OrcsAI(GameAI):
    def build_structures(self):
        """build structures"""

    def build_units(self):
        """build units"""

    def send_scouts(self, position: Any):
        """additional scout processing"""
        return super().send_scouts(position)

    def send_warriors(self, position: Any):
        """additional warriors processing"""
        return super().send_warriors(position)


class MonstersAI(GameAI):
    def collect_resources(self):
        """extra collect resources"""
        return super().collect_resources()

    def build_structures(self):
        """build structures"""

    def build_units(self):
        """build units"""

    def send_scouts(self, position: Any):
        """additional scout processing"""
        return super().send_scouts(position)

    def send_warriors(self, position: Any):
        """additional warriors processing"""
        return super().send_warriors(position)


"""
Inheritance is the base for template method.
"""
