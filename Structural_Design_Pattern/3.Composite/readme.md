# Composite

[*Structural Design Pattern*]

Composite is a structural design pattern that lets you compose
objects into tree structures and then work with these
structures as if they were individual objects

```mermaid
classDiagram
    class Client

    class Component
    <<Interface>> Component
    Component: +execute()

    class Leaf
    Leaf: +execute()

    class Composite
    Composite: +children#58; Component[]
    Composite: +add(Component)
    Composite: +remove(Component)
    Composite: +get_children()
    Composite: +execute()

    Client --> Component
    Component <|.. Leaf
    Component <|.. Composite
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class ImageEditor

    class Graphic
    <<Interface>> Graphic
    Graphic: +move(x,y)
    Graphic: +draw()

    class Dot
    Dot: +x
    Dot: +y
    Dot: move(x,y)
    Dot: draw()

    class CompoundGraphic
    CompoundGraphic: +children#58; Graphic[]
    CompoundGraphic: +add(Graphic)
    CompoundGraphic: +remove(Graphic)
    CompoundGraphic: +move(x,y)
    CompoundGraphic: +draw()

    class Circle
    Circle: +radius
    Circle: +draw()

    ImageEditor --> Graphic
    Graphic <|.. Dot
    Graphic <|.. CompoundGraphic
    Dot <|-- Circle
```

Here, using composition we can create complex data structure
by nesting data one inside another. Here the compound graphic
can be formed by composition of zero or many Graphic content