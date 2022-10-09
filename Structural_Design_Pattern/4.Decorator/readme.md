# Decorator/Wrapper

[*Structural Design Pattern*]

Decorator is a structural design pattern that lets you attach
new behaviours to objects by placing these objects inside
special wrapper objects that contain the behaviours.

```mermaid
classDiagram
    class Client

    class Component
    <<Interface>> Component
    Component: +execute()

    class ConcreteComponent
    ConcreteComponent: +execute()

    class BaseDecorator
    BaseDecorator: +wrapee#58; Component
    BaseDecorator: +Decorator(Component)
    BaseDecorator: +execute()

    class ConcreteDecorators
    ConcreteDecorators: +execute()
    ConcreteDecorators: +extra()

    Client --> Component
    Component <|.. ConcreteComponent
    Component <|.. BaseDecorator
    BaseDecorator <|-- ConcreteDecorators
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class Client

    class DataSource
    <<Interface>> DataSource
    DataSource: +write_data(data)
    DataSource: +read_data()

    class FileDataSource
    FileDataSource: +filename
    FileDataSource: +write_data(data)
    FileDataSource: +read_data()

    class DataSourceDecorator
    DataSourceDecorator: +wrappee#58; DataSource
    DataSourceDecorator: DataSourceDecorator(DataSource)
    DataSourceDecorator: +write_data(data)
    DataSourceDecorator: +read_data()

    class EncryptionDecorator
    EncryptionDecorator: +write_data(data)
    EncryptionDecorator: +read_data()

    class CompressionDecorator
    CompressionDecorator: +write_data(data)
    CompressionDecorator: +read_data()

    Client --> DataSource
    DataSource <|.. FileDataSource
    DataSource <|.. DataSourceDecorator
    DataSourceDecorator <|-- EncryptionDecorator
    DataSourceDecorator <|-- CompressionDecorator
```

In this pattern, the base functionality of the class, i.e.
data read and write is extended by the Decorator classes.
The DataSourceDecorator wraps the FileDataSource and provides
additional functionalities like encryption or compression to
the data.