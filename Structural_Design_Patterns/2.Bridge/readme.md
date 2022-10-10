# Bridge

[*Structural Design Pattern*]


Bridge is a structural design pattern that lets you split a large
class or a set of closely related classes into two seperate
hierarchies - abstraction and implementation - which can be
developed independently of each other.

```mermaid
classDiagram
    class Client

    class Remote
    Remote: +device#58; Device
    Remote: +toggle_power()
    Remote: +volume_up()
    Remote: +volume_down()
    Remote: +channel_up()
    Remote: +channel_down()

    class AdvancedRemote
    AdvancedRemote: +mute()

    Client --> Remote
    Remote <|-- AdvancedRemote

    class Device
    <<Interface>> Device
    Device: +is_enabled()
    Device: +enable()
    Device: +disable()
    Device: +get_volume()
    Device: +set_volume(percentage)
    Device: +get_channel()
    Device: +set_channel()

    class Radio
    Radio: +is_enabled()
    Radio: +enable()
    Radio: +disable()
    Radio: +get_volume()
    Radio: +set_volume(percentage)
    Radio: +get_channel()
    Radio: +set_channel()

    class TV
    TV: +is_enabled()
    TV: +enable()
    TV: +disable()
    TV: +get_volume()
    TV: +set_volume(percentage)
    TV: +get_channel()
    TV: +set_channel()

    Device <|.. Radio
    Device <|.. TV

    Remote o--> Device

```

This pattern seems similar to that of adapter pattern. 
It varies as the pattern works on large number of closely
related classes. In this given example, Radio and TV are
closely related classes.
