# Template Method

[*Behavioural Design Pattern*]

Template Method is a behavioural design pattern that defines
the skeleton of an algorithm in the superclass but lets
subclasses override specific steps of the algorithm without
changing its structure.


```mermaid
classDiagram
    class AbstractClass
    AbstractClass: +template_method()
    AbstractClass: +step1()
    AbstractClass: +step2()
    AbstractClass: +step3()

    class ConcreteClass1
    ConcreteClass1: +step3()

    class ConcreteClass2
    ConcreteClass2: +step1()
    ConcreteClass2: +step2()
    ConcreteClass2: +step3)

    AbstractClass <|-- ConcreteClass1
    AbstractClass <|-- ConcreteClass2
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class GameAI
    GameAI: +take_turn()
    GameAI: +collect_resources()
    GameAI: +build_structures()*
    GameAI: +build_units()*
    GameAI: +attack()
    GameAI: +send_scouts(position)
    GameAI: +send_warriors(position)

    class OrcsAI
    OrcsAI: +build_structures()
    OrcsAI: +build_units()
    OrcsAI: +send_scouts(position)
    OrcsAI: +send_warriors(position)

    class MonstersAI
    MonstersAI: +collect_resources()
    MonstersAI: +build_structures()
    MonstersAI: +build_units()
    MonstersAI: +send_scouts(position)
    MonstersAI: +send_warriors(position)

    GameAI <|-- OrcsAI
    GameAI <|-- MonstersAI
```

Inheritance is the base for template method.