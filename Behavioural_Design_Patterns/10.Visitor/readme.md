# Visitor

[*Behavioural Design Pattern*]

Visitor is a behavioural design pattern that lets you seperate
algorithms from the objects on which they operate.


```mermaid
classDiagram
    class Client

    class Visitor
    <<Interface>> Visitor
    Visitor: +visit(ElementA)
    Visitor: +visit(ElementB)

    class Element
    <<Interface>> Element
    Element: +accept(Visitor)

    class ElementA
    ElementA: +featureA()
    ElementA: +accept(Visitor)

    class ElementB
    ElementB: +featureB()
    ElementB: +accept(Visitor)

    class ConcreteVisitors
    ConcreteVisitors: +visit(ElementA)
    ConcreteVisitors: +visit(ElementB)

    Client --> ConcreteVisitors
    Client --> Element
    Element --> Visitor
    Visitor <|.. ConcreteVisitors
    Element <|.. ElementA
    Element <|.. ElementB
    Visitor --> ElementA
    Visitor --> ElementB
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class Application

    class Visitor
    <<Interface>> Visitor
    Visitor: +visit_dot(Dot)
    Visitor: +visit_circle(Circle)
    Visitor: +visit_rectangle(Rectangle)
    Visitor: +visit_compound_graphics(CompoundGraphic)

    class Shape
    <<Interface>> Shape
    Shape: +move(x, y)
    Shape: +draw()
    Shape: +accept(Visitor)

    class Dot
    Dot: +move(x, y)
    Dot: +draw()
    Dot: +accept(Visitor)

    class Circle
    Circle: +move(x, y)
    Circle: +draw()
    Circle: +accept(Visitor)

    class Rectangle
    Rectangle: +move(x, y)
    Rectangle: +draw()
    Rectangle: +accept(Visitor)

    class CompoundShape
    CompoundShape: +move(x, y)
    CompoundShape: +draw()
    CompoundShape: +accept(Visitor)

    class XMLExportVisitor
    XMLExportVisitor: +visit_dot(Dot)
    XMLExportVisitor: +visit_circle(Circle)
    XMLExportVisitor: +visit_rectangle(Rectangle)
    XMLExportVisitor: +visit_compound_graphics(CompoundGraphic)

    Application --> XMLExportVisitor
    Application --> Shape
    Visitor <|.. XMLExportVisitor
    Shape --> Visitor
    Visitor --> Dot
    Visitor --> Circle
    Visitor --> Rectangle
    Visitor --> CompoundShape
    Shape <|.. Dot
    Shape <|.. Circle
    Shape <|.. Rectangle
    Shape <|.. CompoundShape

```