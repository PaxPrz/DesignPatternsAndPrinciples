from dataclasses import dataclass
from typing import Protocol


class Strategy(Protocol):
    def execute(self, a: int, b: int) -> float:
        ...


class ConcreteStrategyAdd:
    def execute(self, a: int, b: int) -> float:
        return a + b


class ConcreteStrategySubtract:
    def execute(self, a: int, b: int) -> float:
        return a - b


class ConcreteStrategyMultiply:
    def execute(self, a: int, b: int) -> float:
        return a * b


class ConcreteStrategyDivision:
    def execute(self, a: int, b: int) -> float:
        return a / b


@dataclass
class Context:
    strategy: Strategy = None

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, a: int, b: int) -> float:
        return self.strategy.execute(a, b)


"""
Strategy pattern is similar to that of State but one strategy
does not know about another strategy.
"""


if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    context = Context()
    context.set_strategy(ConcreteStrategyAdd())
    print(context.execute_strategy(a, b))

    context.set_strategy(ConcreteStrategySubtract())
    print(context.execute_strategy(a, b))

    context.set_strategy(ConcreteStrategyMultiply())
    print(context.execute_strategy(a, b))

    context.set_strategy(ConcreteStrategyDivision())
    print(context.execute_strategy(a, b))
