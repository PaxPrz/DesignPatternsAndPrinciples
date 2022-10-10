# Memento / Snapshot

[*Behavioural Design Pattern*]

Memento is a behavioural design pattern that lets you save and
restore the previous state of an object without revealing the
details of its implementation.

```mermaid
classDiagram
    class Memento
    <<Interface>> Memento
    Memento: +get_name()
    Memento: +get_snapshot_date()

    class Snapshot
    Snapshot: +text
    Snapshot: +current_pos
    Snapshot: +selection
    Snapshot: +current_font
    Snapshot: +styles

    class Editor
    Editor: +text
    Editor: +current_pos
    Editor: +selection
    Editor: +current_font
    Editor: +styles
    Editor: +make_snapshot()
    Editor: +restore(Memento)

    class History

    class Command

    Memento <|.. Snapshot
    Command --> Editor
    History --> Memento
    Editor <..> Snapshot
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class Editor
    Editor: +state
    Editor: +get_state()
    Editor: +create_snapshot()
    
    class Snapshot
    Snapshot: +state
    Snapshot: +Snapshot(state)
    Snapshot: +restore()

    class Command
    Command: +backup#58; Snapshot
    Command: +make_backup()
    Command: +undo()
    
    Editor <--> Snapshot
    Command --> Snapshot
```

Memento pattern is useful when you want to produce snapshot
of object's state to be able to restore a previous state
of the object.
