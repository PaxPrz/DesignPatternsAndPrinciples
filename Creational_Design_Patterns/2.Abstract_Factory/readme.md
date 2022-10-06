# Abstract Factory

[*Creational Design Pattern*]

Abstract Factory is a creational design pattern that lets you
produce families of related objects without specifying
their concrete classes.

```mermaid
classDiagram
    class Chair
    <<Interface>> Chair
    Chair: +has_legs()
    Chair: +sit_on()

    class VictorianChair
    VictorianChair: +has_legs()
    VictorianChair: +sit_on()

    class ModernChair
    ModernChair: +has_legs()
    ModernChair: +sit_on()

    Chair <|..  VictorianChair
    Chair <|..  ModernChair

    class Sofa
    <<Interface>> Sofa
    Sofa: +sit_count()

    class VictorianSofa
    VictorianSofa: +sit_count()

    class ModernSofa
    ModernSofa: +sit_count()

    Sofa <|.. VictorianSofa
    Sofa <|.. ModernSofa

    class FurnitureFactory
    <<Interface>> FurnitureFactory
    FurnitureFactory: +make_chair()
    FurnitureFactory: +make_sofa()

    class VictorianFurnitureFactory
    VictorianFurnitureFactory: +make_chair()
    VictorianFurnitureFactory: +make_sofa()

    class ModernFurnitureFactory
    ModernFurnitureFactory: +make_chair()
    ModernFurnitureFactory: +make_sofa()

    FurnitureFactory <|.. VictorianFurnitureFactory
    FurnitureFactory <|.. ModernFurnitureFactory

    VictorianFurnitureFactory --> VictorianChair
    VictorianFurnitureFactory --> VictorianSofa

    ModernFurnitureFactory --> ModernChair
    ModernFurnitureFactory --> ModernSofa

    class Application
    Application: +factory#58; FurnitureFactory
    Application o--> FurnitureFactory
```

This pattern is similar to that of Factory Creation Pattern,
but the factory here encompasses all the similarly grouped classes.
So for example if a client chooses victorian set, it'll only get
victorian chair and sofa for the entire phase. Similar example can
be observed for GUI design between Windows OS and Linux. As for a
specific OS, the buttons, panels, textbox, etc must of one of the
groups.