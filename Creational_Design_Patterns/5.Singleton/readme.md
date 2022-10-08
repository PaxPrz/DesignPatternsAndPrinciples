# Singleton

[*Creational Design Pattern*]

Singleton is a creational design pattern that lets you ensure
that a class has only one instance, while providing a global
access point to this instance.

```mermaid
classDiagram
    class Singleton
    Singleton: +instance#58; Singleton
    Singleton: +Singleton()
    Singleton: +get_instance() Singleton
```

In this approach, when the class is instantiated for first time,
the initializer method is called and all the necessary parameters
are initialized. Later on, whenever the application reinstantiate
the class, the same object is returned to the context.