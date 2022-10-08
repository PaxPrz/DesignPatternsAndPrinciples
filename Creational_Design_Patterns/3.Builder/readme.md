# Builder

[*Creational Design Pattern*]

Builder is a creational design pattern that lets you construct
complex objects step by step. Thus, the pattern allows you to
produce different types and representations of an object using
the same construction code.

```mermaid
classDiagram
    class HouseBuilder
    <<Interface>> HouseBuilder
    HouseBuilder: +reset()
    HouseBuilder: +build_walls()
    HouseBuilder: +build_doors()
    HouseBuilder: +build_windows()
    HouseBuilder: +build_roof()
    HouseBuilder: +build_gate()
    HouseBuilder: +get_result()

    class HallBuilder
    HallBuilder: result#58; Hall
    HallBuilder: +reset()
    HallBuilder: +build_walls()
    HallBuilder: +build_doors()
    HallBuilder: +build_windows()
    HallBuilder: +build_roof()
    HallBuilder: +build_gate()
    HallBuilder: +get_result()

    class GarageBuilder
    GarageBuilder: result#58; Hall
    GarageBuilder: +reset()
    GarageBuilder: +build_walls()
    GarageBuilder: +build_doors()
    GarageBuilder: +build_windows()
    GarageBuilder: +build_roof()
    GarageBuilder: +build_gate()
    GarageBuilder: +get_result()

    HouseBuilder <|.. HallBuilder
    HouseBuilder <|.. GarageBuilder

    class Hall
    Hall: +doors
    Hall: +windows
    Hall: +walls
    Hall: +roof

    class Garage
    Garage: +gates
    Garage: +walls
    Garage: +roof

    HallBuilder --> Hall
    GarageBuilder --> Garage

    class Director
    Director: +builder#58; HouseBuilder
    Director: +Director(builder)
    Director: +change_builder(builder)
    Director: +make(type)

    Director o-- HouseBuilder

```

According to this pattern, the creation of an class is assigned
to a builder class. The builder has different methods according
to which the instance can have different property after it's creation
gets completed. Here HouseBuilder is implemented by
HallBuilder and GarageBuilder. And accordingly build the respective
object of Hall or Garage with its properties.
Additionally, we can have a Director class, that store the base
rules for creating object with specific properties.