# Inteface Segregation Principle


### Before

```mermaid
classDiagram
    class CloudProvider
    <<Interface>> CloudProvider
    CloudProvider: +store_file(name)
    CloudProvider: +get_file(name)
    CloudProvider: +create_server(region)
    CloudProvider: +list_servers(region)
    CloudProvider: +get_cdn_address()

    class Amazon
    Amazon: +store_file(name)
    Amazon: +get_file(name)
    Amazon: +create_server(region)
    Amazon: +list_servers(region)
    Amazon: +get_cdn_address()

    class DropBox
    DropBox: +store_file(name)
    DropBox: +get_file(name)

    CloudProvider <|.. Amazon
    CloudProvider <|.. DropBox
```

When this system was designed, maybe the system only required CloudProvider
to provide services to store and retrive files. So client designed a interface
with store and get method and implemented Amazon and Dropbox.
As program gets larger and added with functionality, it was realized that
we may now need to create servers and use CDN too. But dropbox didn't provided these
services. And theoritically storing data and creating server are two different
domain things. This will eventually create bug in code.


### After

```mermaid
classDiagram
    class CloudStorageProvider
    <<Interface>> CloudStorageProvider
    CloudStorageProvider: +store_file(name)
    CloudStorageProvider: +get_file(name)

    class CloudHostingProvider
    <<Interface>> CloudHostingProvider
    CloudHostingProvider: +create_server(region)
    CloudHostingProvider: +list_servers(region)

    class CDNProvider
    <<Interface>> CDNProvider
    CDNProvider: +get_cdn_address()

    class Amazon
    Amazon: +store_file(name)
    Amazon: +get_file(name)
    Amazon: +create_server(region)
    Amazon: +list_servers(region)
    Amazon: +get_cdn_address()

    class DropBox
    DropBox: +store_file(name)
    DropBox: +get_file(name)

    CloudStorageProvider <|.. Amazon
    CloudStorageProvider <|.. DropBox
    CloudHostingProvider <|.. Amazon
    CDNProvider <|.. Amazon
```

This principle focuses on segregation of interface so that
a class only implements certain inteface to its full. Since DropBox
now does not implement CloudHostingProvider or CDNProvider we now
cannot pass DropBox instance to functions that use these object to create
server or get CDN.