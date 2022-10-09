# Flyweight

[*Structural Design Pattern*]

Flyweight is a structural design pattern that lets you fit more
objects into the available amount of RAM by sharing common
parts of state between multiple objects instead of keeping all
of the data in each objects.


```mermaid
classDiagram
    class Flyweight
    Flyweight: +repeating_state
    Flyweight: +operation(unique_state)

    class Context
    Context: +unique_state
    Context: +flyweight
    Context: +operation()

    class FlyweightFactory
    FlyweightFactory: +cache#58; Flyweight[]
    FlyweightFactory: +get_flyweight(repeating_state)

    class Client

    Client o--> Context
    Context --> Flyweight
    Context --> FlyweightFactory
    FlyweightFactory o--> Flyweight
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class TreeType
    TreeType: +name
    TreeType: +color
    TreeType: +texture
    TreeType: +draw(canvas, x, y)

    class Tree
    Tree: +x
    Tree: +y
    Tree: +type#58; TreeType
    Tree: +draw(canvas)

    class TreeFactory
    TreeFactory: +tree_types#58; TreeType[]
    TreeFactory: +get_tree_type(name, color, texture)

    class Forest
    Forest: +trees#58; Tree[]
    Forest: +plant_tree(x, y, name, color, texture) Tree
    Forest: +draw(canvas)

    Forest o--> Tree
    Tree --> TreeFactory
    Tree --> TreeType
    TreeFactory o--> TreeType
```

Using this Flyweight pattern, the common attributes are reused
by the system. Those attributes whose value does not change
once initialized can be used as flyweight and reused in another
objects. Here TreeType is a flyweight as the name, color and texture
of a particular tree is same and do not need to be stored in multiple
RAM location.
