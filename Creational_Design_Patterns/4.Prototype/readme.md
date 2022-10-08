# Prototype

[*Creational Design Pattern*]

Prototype is a creational design pattern that lets you copy
existing objects without making your code dependent on
their classes.


```mermaid
classDiagram
    class Prototype
    <<Interface>> Prototype
    Prototype: +clone() Prototype

    class Shape
    <<Abstract>> Shape
    Shape: +x
    Shape: +y
    Shape: +Shape(source)
    Shape: +clone()

    class Rectangle
    Rectangle: +width
    Rectangle: +height
    Rectangle: +Rectangle()
    Rectangle: +clone()

    class Circle
    Circle: +radius
    Circle: +Circle()
    Circle: +clone()

    Prototype <|.. Shape
    Shape <|-- Rectangle
    Shape <|-- Circle
    
```

For a large and complicated initialization required for an class,
this pattern can be implemented. This will simplify the creation
as it creates object by cloning and existing object. The required
class implements the Prototype class that implements the clone
method.