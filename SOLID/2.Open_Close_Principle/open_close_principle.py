from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import List, Protocol


@dataclass
class Order:
    line_items: List[str]
    shipping: str

    def get_total(self) -> float:
        ...

    def get_shipping_cost(self) -> float:
        if self.shipping == "ground":
            ...
        elif self.shipping == "air":
            ...

    def get_arrival_date(self) -> datetime:
        if self.shipping == "ground":
            ...
        elif self.shipping == "air":
            ...


"""
An class should be open for extension but closed for modification.
This is the motto of this principle. Here as we can see, if we need 
to add another shipping method in future let's say by 'waterways',
we need to update the Order class which is not a good way.
"""


class Shipping(Protocol):
    def get_cost(self, order: Order) -> float:
        ...

    def get_arrival_date(self: Order) -> datetime:
        ...


class Ground:
    def get_cost(self, order: Order) -> float:
        ...

    def get_arrival_date(self: Order) -> datetime:
        ...


class Air:
    def get_cost(self, order: Order) -> float:
        ...

    def get_arrival_date(self: Order) -> datetime:
        ...


@dataclass
class Order:
    line_items: List[str]
    shipping: Shipping

    def get_total(self) -> float:
        ...

    def get_shipping_cost(self) -> float:
        self.shipping.get_cost(self)

    def get_arrival_date(self) -> datetime:
        self.shipping.get_arrival_date(self)


"""
Now here, shipping actually is an object that has all the
necessary functions defined using an interface (protocol).
If new shipping method are further added to the system, we now need
no modification in order class. Instead we implement Shipping interface
for our new 'waterways' shipping method
"""


class WaterWays:
    def get_cost(self, order: Order) -> float:
        ...

    def get_arrival_date(self, order: Order) -> datetime:
        ...
