
# Proxy

[*Structural Design Pattern*]

Proxy is a structural design pattern that lets you provide a
substitute or placeholder for another object. A proxy controls
access to the original object, allowing you to perform 
something else before or after the request gets through to
the original object.


```mermaid
classDiagram
    class Client

    class ServiceInterface
    <<Interface>> ServiceInterface
    ServiceInterface: +operation()

    class Proxy
    Proxy: +real_service#58; Service
    Proxy: +check_access()
    Proxy: +operation()

    class Service
    Service: +operation()

    Client --> ServiceInterface
    ServiceInterface <|.. Proxy
    ServiceInterface <|.. Service
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class YoutubeManager

    class ThirdPartyYoutubeLib
    <<Interface>> ThirdPartyYoutubeLib
    ThirdPartyYoutubeLib: +list_videos()
    ThirdPartyYoutubeLib: +get_video_info(id)
    ThirdPartyYoutubeLib: +download_video(id)

    class CachedYoutubeClass
    CachedYoutubeClass: +service#58; ThirdPartyYoutubeLib
    CachedYoutubeClass: +list_videos()
    CachedYoutubeClass: +get_video_info(id)
    CachedYoutubeClass: +download_video(id)

    class ThirdPartyYoutubeClass
    ThirdPartyYoutubeClass: +list_videos()
    ThirdPartyYoutubeClass: +get_video_info(id)
    ThirdPartyYoutubeClass: +download_video(id)

    YoutubeManager --> ThirdPartyYoutubeLib
    ThirdPartyYoutubeLib <|.. CachedYoutubeClass
    ThirdPartyYoutubeLib <|.. ThirdPartyYoutubeClass
    CachedYoutubeClass o--> ThirdPartyYoutubeClass
```

In Proxy pattern, the actual service is overwrapped by proxy
object. The proxy object then decides whether to process on its own
or use the actual object to process.