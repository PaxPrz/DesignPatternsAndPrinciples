from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Protocol


class Transport(Protocol):
    def deliver(self, *items):
        ...


class Truck:
    def deliver(self, *items):
        """deliver in Truck"""
        print(f"Delivering Items in Truck: {items}")


class Ship:
    def deliver(self, *items):
        """deliver in Ship"""
        print(f"Delivering Items in Ship: {items}")


@dataclass(init=False)
class Logistics(ABC):
    cargos: List[str]

    def __init__(self, cargos: List[str] = []):
        self.cargos = cargos

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver(*self.cargos)

    @abstractmethod
    def create_transport(self) -> Transport:
        raise NotImplementedError


class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


if __name__ == "__main__":
    cargos = ["apple", "ball"]
    choice = input("Choose Road or Sea (Road/Sea): ")
    if choice.lower() == "road":
        app: Logistics = RoadLogistics(cargos=cargos)
    elif choice.lower() == "sea":
        app: Logistics = SeaLogistics(cargos=cargos)
    else:
        raise ValueError("Invalid way")
    app.plan_delivery()

'''
In Factory Method Creational Pattern, the creation of Transport
object is deligated to another class i.e. Logistics class.
The overall logic for delivery in implemented on deliver method
and the correct Transport is created by respective creation factory.
'''