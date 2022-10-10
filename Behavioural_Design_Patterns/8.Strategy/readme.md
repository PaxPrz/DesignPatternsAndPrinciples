# Strategy

[*Behavioural Design Pattern*]

Strategy is the behavioural design pattern that lets you define
a family of algorithms, put each of them into seperate class,
and make their objects interchangeable.

```mermaid
classDiagram
    class Client

    class Context
    Context: +strategy
    Context: +set_strategy(Strategy)
    Context: +do_something()

    class Strategy
    <<Interface>> Strategy
    Strategy: +execute(data)

    class ConcreteStrategies
    ConcreteStrategies: +execute(data)

    Client --> Context
    Client --> ConcreteStrategies
    Context o--> Strategy
    Strategy <|.. ConcreteStrategies
```

Strategy pattern is similar to that of State but one strategy
does not know about another strategy.