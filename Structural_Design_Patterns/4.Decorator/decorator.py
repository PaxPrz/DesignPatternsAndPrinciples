from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol
import zlib
from Crypto.Cipher import AES
from hashlib import sha256


class DataSource(Protocol):
    def write_data(self, data: bytes) -> None:
        ...

    def read_data(self) -> bytes:
        ...


@dataclass
class FileDataSource:
    filename: str

    def write_data(self, data: bytes) -> None:
        with open(self.filename, "wb") as f:
            f.write(data)

    def read_data(self) -> bytes:
        with open(self.filename, "rb") as f:
            data = f.read()
        return data


@dataclass
class DataSourceDecorator(ABC):
    wrappee: DataSource

    @abstractmethod
    def write_data(self, data) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_data(self) -> bytes:
        raise NotImplementedError


@dataclass(init=False)
class EncryptionDecorator(DataSourceDecorator):
    encryption_key: bytes

    def __init__(self, wrappee: DataSource, encryption_key: str):
        super().__init__(wrappee)
        hash = sha256(encryption_key.encode()).hexdigest()[:16]
        self.encryption_key = hash.encode()

    def write_data(self, data: bytes) -> None:
        aes = AES.new(self.encryption_key, AES.MODE_EAX)
        encrypted = aes.encrypt(data)
        self.wrappee.write_data(encrypted)

    def read_data(self) -> bytes:
        encrypted = self.wrappee.read_data()
        aes = AES.new(self.encryption_key, AES.MODE_EAX)
        data = aes.decrypt(encrypted)
        return data


@dataclass
class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data: bytes) -> None:

        compressed = zlib.compress(data)
        self.wrappee.write_data(compressed)

    def read_data(self) -> bytes:
        compressed = self.wrappee.read_data()
        data = zlib.decompress(compressed)
        return data


"""
In this pattern, the base functionality of the class, i.e.
data read and write is extended by the Decorator classes.
The DataSourceDecorator wraps the FileDataSource and provides
additional functionalities like encryption or compression to
the data.
"""


if __name__ == "__main__":
    filename = input("Enter filename: ") + ".tempfile"
    source = FileDataSource(filename)
    content = input("Write some content: ").encode()
    if is_encrypt := input("Do you want to encrypt (y/n): ").lower() in ["yes", "y"]:
        encryption_key = input("Provide Encryption key: ")
        source = EncryptionDecorator(source, encryption_key)
    if is_compress := input("Do you want to compress (y/n): ").lower() in ["yes", "y"]:
        source = CompressionDecorator(source)
    source.write_data(content)

    print(source.read_data())
