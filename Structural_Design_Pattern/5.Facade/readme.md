# Facade

[*Structural Design Pattern*]

Facade is a structural design pattern that provides a
simplified interface to a library, a framework, or
any other complex set of classes


```mermaid
classDiagram
    class Client

    class Facade
    Facade: +links_to_subsystem_objects
    Facade: +optional_additional_facade
    Facade: +subsystem_operation()

    class AdditionalFacade
    AdditionalFacade: +another_operation()

    class SubSystemClass1

    class SubSystemClass2

    class SubSystemClass3

    Facade ..> SubSystemClass1
    Facade ..> SubSystemClass2
    Facade ..> SubSystemClass3
    AdditionalFacade ..> SubSystemClass3

    Client --> Facade
    Facade --> AdditionalFacade
```

The above diagram can be interpreted into example below.

```mermaid
classDiagram
    class Application

    class VideoConverter
    VideoConverter: +convert_video(filename, format)

    class AudioMixer
    class VideoFile
    class BitrateReader
    class CodecFactory
    class OggCompressionCodec
    class MPEG4CompressionCodec

    Application --> VideoConverter
    VideoConverter ..> AudioMixer
    VideoConverter ..> VideoFile
    VideoConverter ..> BitrateReader
    VideoConverter ..> CodecFactory
    VideoConverter ..> OggCompressionCodec
    VideoConverter ..> MPEG4CompressionCodec
```

Facade is useful if you need to work with large number of complex
classes. It is useful to work with legacy systems also. Facade works
as an adapter to entire subsytem of objects.
