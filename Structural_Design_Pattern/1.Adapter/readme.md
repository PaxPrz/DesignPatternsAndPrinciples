# Adapter

[*Structural Design Pattern*]

Adapter is a structural design pattern that allows
objects with incompatible interfaces to collaborate.


```mermaid
classDiagram
    class Service
    Service: +service_method(special_data)

    class ClientInterface
    <<Interface>> ClientInterface
    ClientInterface: +method(data)

    class Adapter
    Adapter: +adaptee#58; Service
    Adapter: +method(data)

    class Client

    ClientInterface <|.. Adapter
    Adapter o--> Service
    Client --> ClientInterface
```

Similar structure can be achieved as below

```mermaid
classDiagram
    class Users
    <<SqlalchemyService>> Users
    Users: +execute()
    Users: +fetchall()

    class Repository
    <<ClientInterface>> Repository
    Repository: +get(id)
    Repository: +list()
    Repository: +create(model)
    Repository: +update(model)

    class UserSqlRepository
    <<Adapter>> UserSqlRepository
    UserSqlRepository: +db#58; Service
    UserSqlRepository: +get(id)
    UserSqlRepository: +list()
    UserSqlRepository: +create(model)
    UserSqlRepository: +update(model)

    class Client

    Client --> Repository
    Repository <|.. UserSqlRepository
    UserSqlRepository o--> Users
```

In this structural pattern, the client depends on an interface
for a third party service. In this given example of SqlAlchemy,
the users is a third party service in which the client is dependent on.
But It will quickly be mess if client calls straight to the
third party service functions. So client actually depend on the
abstraction over an adapter, which infact connect the client to
the actual functions in the service. Thus, the service are now
swappable for client by implementing another adapter.