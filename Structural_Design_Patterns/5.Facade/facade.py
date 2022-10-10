class VideoFile:
    """Video Library"""


class OggCompressionCodec:
    """Ogg Compression Codec Library"""


class MPEG4CompressionCodec:
    """MPEG4 Compression Codec Library"""


class CodecFactory:
    """Codec Library"""


class BitrateReader:
    """Bitrate Reader Library"""


class AudioMixer:
    """Audio Mixer Library"""


class VideoConverter:
    def convert(filename: str, format: str) -> str:
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)
        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(result)
        return VideoFile(result)


"""
Facade is useful if you need to work with large number of complex
classes. It is useful to work with legacy systems also. Facade works
as an adapter to entire subsytem of objects.
"""


if __name__ == "__main__":
    converter = VideoConverter()
    mp4 = converter.convert("videofile.ogg", "mp4")
    mp4.save()
