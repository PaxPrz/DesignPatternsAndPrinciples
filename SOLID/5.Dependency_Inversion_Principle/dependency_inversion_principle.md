# Dependency Inversion Principle

High-level classes shouldn't depend on low-level classes.
Both should depend on abstractions. Abstractions shouldn't
depend on details. Details should depend on abstractions.

### Before

```mermaid
classDiagram
    class APIIntegrator
    APIIntegrator: +url
    APIIntegrator: +data
    APIIntegrator: +get()
    APIIntegrator: +create()
```
Instead of APIIntegrator depend on request library, here the dependency
is inversed. APIIntegrator now depend on HTTPClient which is an abstraction
over request library. Now in future, if we need to change the low-level
class like requests, we just need to change the client in APIIntegrator.
Besides it also support for unit testing APIIntegrator module as for test
we can provide fake client.

### After

```mermaid
classDiagram
    class APIIntegrator
    APIIntegrator: +url
    APIIntegrator: +data
    APIIntegrator: +client#58; HTTPClient
    APIIntegrator: +get()
    APIIntegrator: +create()

    class HTTPClient
    <<Interface>> HTTPClient
    HTTPClient: +get(url)
    HTTPClient: +post(url, data)

    class RequestClient
    RequestClient: +get(url)
    RequestClient: +post(url, data)

    class FakeClient
    FakeClient: +get(url)
    FakeClient: +post(url, data)

    HTTPClient <|.. RequestClient
    HTTPClient <|.. FakeClient
    APIIntegrator o-- HTTPClient
```
