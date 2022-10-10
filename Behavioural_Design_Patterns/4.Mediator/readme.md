# Mediator / Intermediary / Controller

[*Behavioural Design Pattern*]

Mediator is a behavioural design pattern that lets you reduce
chaotic dependencides between objects. The pattern restricts
direct communications between the objects and forces them to
collaborate only via a mediator object.


```mermaid
classDiagram
    class Mediator
    <<Interface>> Mediator
    Mediator: +notify(sender)

    class ConcreteMediator
    ConcreteMediator: +componentA
    ConcreteMediator: +componentB
    ConcreteMediator: +componentC
    ConcreteMediator: +componentD
    ConcreteMediator: +notify(sender)
    ConcreteMediator: +react_on_A()
    ConcreteMediator: +react_on_B()
    ConcreteMediator: +react_on_C()
    ConcreteMediator: +react_on_D()

    class ComponentA
    ComponentA: m#58; Mediator
    ComponentA: operationA()

    class ComponentB
    ComponentB: m#58; Mediator
    ComponentB: operationB()

    class ComponentC
    ComponentC: m#58; Mediator
    ComponentC: operationC()

    class ComponentD
    ComponentD: m#58; Mediator
    ComponentD: operationD()

    Mediator <|.. ConcreteMediator
    ConcreteMediator --> ComponentA
    ConcreteMediator --> ComponentB
    ConcreteMediator --> ComponentC
    ConcreteMediator --> ComponentD
    ComponentA --> Mediator
    ComponentB --> Mediator
    ComponentC --> Mediator
    ComponentD --> Mediator
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class Mediator
    <<Interface>> Mediator
    Mediator: +notify(sender#58; Component, event#58; string)

    class AuthenticationDialog
    AuthenticationDialog: +title
    AuthenticationDialog: +login_or_register#58; Checkbox
    AuthenticationDialog: +login_username, login_password#58; Textbox
    AuthenticationDialog: +reg_username, reg_password, reg_email#58; Textbox
    AuthenticationDialog: +ok, cancel#58; Button
    AuthenticationDialog: +remember_me#58; Checkbox
    AuthenticationDialog: +notify(sender, event)

    class Component
    Component: +dialog#58; Mediator
    Component: click()
    Component: keypress()

    class Button

    class Textbox

    class Checkbox
    Checkbox: +check()

    Mediator <|.. AuthenticationDialog
    Component <--> Mediator
    Mediator <|-- Button
    Mediator <|-- Textbox
    Mediator <|-- Checkbox
    Button o--> AuthenticationDialog
    Textbox o--> AuthenticationDialog
    Checkbox o--> AuthenticationDialog
```

In Mediator pattern, all the action of component is handled by
the mediator object. Here AuthenticationDialog contains all the
components and acts as mediator. A change in any of its component
will trigger notify in the mediator object.