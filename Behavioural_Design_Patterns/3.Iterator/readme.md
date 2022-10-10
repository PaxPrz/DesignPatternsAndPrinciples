# Iterator

[*Behavioural Design Pattern*]

Iterator is a behavioural design pattern that lets you traverse
elements of a collection without exposing its underlying
representation (list, stack, tree, etc)
Python List, Tuples are perfect example for this

```mermaid
classDiagram
    class Client

    class Iterator
    <<Interface>> Iterator
    Iterator: +get_next()
    Iterator: +has_more()

    class IterableCollection
    <<Interface>> IterableCollection
    IterableCollection: +create_iterator() Iterator

    class ConcreteIterator
    ConcreteIterator: +collection#58; ConcreteCollection
    ConcreteIterator: +iteration_state
    ConcreteIterator: +ConcreteIterator(ConcreteCollection)
    ConcreteIterator: +get_next()
    ConcreteIterator: +has_more()

    class ConcreteCollection
    ConcreteCollection: +create_iterator() Iterator

    Client --> Iterator
    Client --> IterableCollection
    Iterator <|.. ConcreteIterator
    IterableCollection <|.. ConcreteCollection
    ConcreteIterator <--> ConcreteCollection
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class SocialNetwork
    <<Interface>> SocialNetwork
    SocialNetwork: +create_friends_iterator(profile_id) ProfileIterator
    SocialNetwork: +create_coworkers_iterator(profile_id) ProfileIterator

    class Iterator
    <<Interface>> Iterator
    Iterator: +get_next() Profile
    Iterator: +has_more() bool

    class Facebook
    Facebook: +create_friends_iterator(profile_id) ProfileIterator
    Facebook: +create_coworkers_iterator(profile_id) ProfileIterator

    class FacebookIterator
    FacebookIterator: +facebook#58; Facebook
    FacebookIterator: +profile_id
    FacebookIterator: +type
    FacebookIterator: +current_position
    FacebookIterator: +cache#58; Profile[]
    FacebookIterator: +lazy_init()
    FacebookIterator: +get_next() Profile
    FacebookIterator: +has_more() bool

    class Profile
    Profile: +get_id()
    Profile: +get_email()

    class SocialSpammer
    SocialSpammer: +send(iterator, message)

    class Application
    Application: +spammer#58; SocialSpammer
    Application: +network
    Application: +send_spam_to_friends(profile)
    Application: +send_spam_to_coworkers(profile)

    Application --> SocialSpammer
    Application --> Facebook
    SocialSpammer --> Profile
    SocialSpammer --> Iterator
    Iterator --> Profile
    Iterator <|-- FacebookIterator
    SocialNetwork --> Iterator
    SocialNetwork <|.. Facebook
    Facebook o--> Profile
    FacebookIterator <--> Facebook

```

Iterator pattern provides a medium to iterator over bunch of
objects in a ordered fashion. Here we've used an example of
mass scammer that sends email to all friends or coworkers
at once. Here we created Iterator for all those categories.
In future, we can also add other Social Media Platform like
LinkedIn, etc.
