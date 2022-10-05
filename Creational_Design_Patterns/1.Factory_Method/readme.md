# Factory Method
[*Creational Design Pattern*]

Factory method patterns suggest that you replace direct object
construction calls with calls to a special factory method.

```mermaid
classDiagram
    class Logistics
    <<Abstract>> Logistics
    Logistics: +cargos
    Logistics: +plan_delivery()
    Logistics: +create_transport()*

    class RoadLogistics
    RoadLogistics: +create_transport()

    class SeaLogistics
    SeaLogistics: +create_transport()

    Logistics <|-- RoadLogistics
    Logistics <|-- SeaLogistics

    class Transport
    <<Interface>> Transport
    Transport: +deliver(*items)

    class Truck
    Truck: +deliver(*items)

    class Ship
    Ship: +deliver(*items)

    Transport <|.. Truck
    Transport <|.. Ship

    Logistics --> Transport

    SeaLogistics --> Ship
    RoadLogistics --> Truck
```

In Factory Method Creational Pattern, the creation of Transport
object is deligated to another class i.e. Logistics class.
The overall logic for delivery in implemented on deliver method
and the correct Transport is created by respective creation factory.