# State

[*Behavioural Design Pattern*]

State is a behavioural design pattern that lets an object alter
its behaviour when its internal state changes. It appears as
if the object changed its class.

```mermaid
classDiagram
    class Client

    class State
    <<Interface>> State
    State: +do_this()
    State: +do_that()

    class ConcreteStates
    ConcreteStates: Document
    ConcreteStates: +render()
    ConcreteStates: +publish()

    class Context
    Context: +state
    Context: +Context(initial_state)
    Context: +do_this()
    Context: +do_that()

    Client --> Context
    Context o--> State
    State <|.. ConcreteStates
    Client --> ConcreteStates
    ConcreteStates --> Context
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class AudioPlayer
    AudioPlayer: +state
    AudioPlayer: +UI, volume, playlist, current_song
    AudioPlayer: +change_state(State)
    AudioPlayer: +click_lock()
    AudioPlayer: +click_play()
    AudioPlayer: +click_next()
    AudioPlayer: +click_previous()
    AudioPlayer: +start_playback()
    AudioPlayer: +stop_playback()
    AudioPlayer: +next_song()
    AudioPlayer: +rewind()

    class State
    State: +player
    State: +click_lock()
    State: +click_play()
    State: +click_next()
    State: +click_previous()

    class ReadyState

    class LockedState

    class PlayingState

    AudioPlayer o--> State
    State <|-- ReadyState
    State <|-- LockedState
    State <|-- PlayingState

```

In State pattern, the overall behaviour of object changes
as the state changes. The action of the objects depend directly
on the state of the object. The state does know about other states
and can transfer the state of Context from one to another.