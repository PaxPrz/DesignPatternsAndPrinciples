# Command / Action / Transaction

[*Behavioural Design Pattern*]

Command is a behavioural design pattern that turns a request
into a stand-alone object that contains all information about
the request. This transformation lets you parameterize
methods with different requests, dleay or quere an request's
execution, and support undoable operations.


```mermaid
classDiagram
    class Client

    class Command
    <<Inteface>> Command
    Command: +execute()

    class Command1
    Command1: +receiver
    Command1: +params
    Command1: +execute()

    class Command2
    Command2: +execute()

    class Invoker
    Invoker: +command
    Invoker: +set_command(Command)
    Invoker: +execute_command()

    class Receiver
    Receiver: +operation(a,b,c)

    Client --> Invoker
    Client --> Receiver
    Client --> Command1
    Command1 --> Receiver
    Invoker o--> Command
    Command <|.. Command1
    Command <|.. Command2

```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class Editor
    Editor: +text
    Editor: +get_selection()
    Editor: +delete_selection()
    Editor: +replace_selection(text)

    class Command
    Command: +app
    Command: +editor
    Command: +backup
    Command: +Command(app, editor)
    Command: +save_backup()
    Command: +undo()
    Command: +execute()*

    class CopyCommand
    CopyCommand: +execute()

    class CutCommand
    CutCommand: +execute()

    class PasteCommand
    PasteCommand: +execute()

    class UndoCommand
    UndoCommand: +execute()

    class CommandHistory
    CommandHistory: +history#58; Command[]
    CommandHistory: +push(Command)
    CommandHistory: +pop() Command

    class Application
    Application: +editors#58; Editor[]
    Application: +active_editor#58; Editor
    Application: +clipboard
    Application: +history#58; CommandHistory
    Application: +create_UI()
    Application: +execute_command(Command)
    Application: +undo()

    Class Buttons

    Class Shortcuts

    Application o--> Editor
    Application o--> CommandHistory
    CommandHistory o--> Command
    Command <|-- CopyCommand
    Command <|-- CutCommand
    Command <|-- PasteCommand
    Command <|-- UndoCommand
    CopyCommand --> Editor
    CutCommand --> Editor
    PasteCommand --> Editor
    UndoCommand --> Application
    Application --> Buttons
    Application --> Shortcuts
    Buttons o--> Command
    Shortcuts o--> Command

```

Command Pattern is useful for queueing operations, scheduling
their executeion or execute them remotely. They also provides
reversible operations.