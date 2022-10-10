# Observer / Event-Subscriber / Listener

[*Behavioural Design Pattern*]

Observer is a behavioural design pattern that lets you define a
subscription mechanism to notify multiple objects without any
events that happen to the object they're observing.

```mermaid
classDiagram
    class Client

    class Publisher
    Publisher: +subscribers#58; Subscribers[]
    Publisher: +main_state
    Publisher: +subscribe(Subscriber)
    Publisher: +unsubscribe(Subscriber)
    Publisher: +notify_subscribers()
    Publisher: +main_business_logic()


    class Subscriber
    <<Interface>> Subscriber
    Subscriber: +update()

    class ConcreteSubscribers
    ConcreteSubscribers: +update()

    Client --> Publisher
    Publisher o--> Subscriber
    Subscriber <|.. ConcreteSubscribers

```

The above diagram can be interpreted into example below.


```mermaid
classDiagram
    class Editor
    Editor: +event_manager
    Editor: +open_file()
    Editor: +save_file()

    class EventManager
    EventManager: +listeners#58; EventListeners[]
    EventManager: +subscribe(event_type, listener)
    EventManager: +unsubscrive(event_type, listener)
    EventManager: +notify(event_type, data)

    class EventListeners
    <<Interface>> EventListeners
    EventListeners: +update(data)

    class EmailAlertsListener
    EmailAlertsListener: +update(data)

    class LoggingListener
    LoggingListener: +update(data)

    Editor o--> EventManager
    EventManager o--> EventListeners
    EventListeners <|.. EmailAlertsListener
    EventListeners <|.. LoggingListener

```

Observer pattern is one of my favourite design patterns.
This pattern can be used from small to large projects.
Reactions that are dependent on action on another domain
can be added as listeners to particular event. Whenever that
particular event occurs, the event_manager will trigger all
the listeners. This works by pushing (triggering) the listener
to perform reaction.