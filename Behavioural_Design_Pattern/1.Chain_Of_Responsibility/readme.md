# Chain Of Responsibility/ Chain of Command

[*Behavioural Design Pattern*]

Chain of Responsibility is a behavioural design pattern that
lets you pass request along a chain of handlers. Upon receiving
a request, each handler decides either to process the request
or to pass it to the next handler in the chain.

```mermaid
classDiagram
    class Client

    class Handler
    <<Interface>> Handler
    Handler: +set_next(Handler)
    Handler: +handle(request)

    class BaseHandler
    BaseHandler: +next#58; Handler
    BaseHandler: +set_next(Handler)
    BaseHandler: +handle(request)

    class ConcreteHandlers
    ConcreteHandlers: +handle(request)

    Client --> Handler
    Handler <|.. BaseHandler
    BaseHandler o--> BaseHandler
    BaseHandler <|-- ConcreteHandlers
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class ComponentWithContextualHelp
    <<Interface>> ComponentWithContextualHelp
    ComponentWithContextualHelp: +show_help()

    class Component
    Component: +container#58; Container
    Component: +tooltip_text
    Component: +show_help()

    class Container
    Container: +children#58; Component
    Container: +add(child)

    class Panel
    Panel: +model_help_text
    Panel: +show_help()

    class Dialog
    Dialog: +wiki_page_url
    Dialog: +show_help()

    class Button
    
    ComponentWithContextualHelp <|.. Component
    Component <|-- Container
    Component <|-- Button
    Container o--> Component
    Component --> Container
    Container <|-- Panel
    Container <|-- Dialog
```

In Chain of Responsibility, the responsibility is serially
transferred to next component. Here in this example, a Panel
have multiple dialogs. In a dialog, there are multiple buttons.
If some button do not have help text, then the respective parent
component (Dialog) help is shown. If the Dialog also do not have
help text, the Panel is given the responsibility. In this chain,
if any one of the component can perform the action. The response
returns from there.