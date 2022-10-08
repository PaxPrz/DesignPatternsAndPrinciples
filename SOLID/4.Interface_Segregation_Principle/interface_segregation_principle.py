from dataclasses import dataclass
from typing import Any, List, Protocol


class CloudProvider(Protocol):
    def store_file(self, name: str) -> bool:
        ...

    def get_file(self, name: str) -> bytes:
        ...

    def create_server(self, region: str) -> Any:
        ...

    def list_servers(self, region: str) -> List[str]:
        ...

    def get_cdn_address(self) -> str:
        ...


@dataclass
class Amazon:
    def store_file(self, name: str) -> bool:
        """stores file in s3"""

    def get_file(self, name: str) -> bytes:
        """get file from s3"""

    def create_server(self, region: str) -> Any:
        """creates ec2 instance"""

    def list_servers(self, region: str) -> List[str]:
        """list ec2 instance"""

    def get_cdn_address(self) -> str:
        """get cdn server url"""


@dataclass
class DropBox:
    def store_file(self, name: str) -> bool:
        """stores file in dropbox"""

    def get_file(self, name: str) -> bytes:
        """get file from dropbox"""

    def create_server(self, region: str) -> Any:
        raise NotImplementedError

    def list_servers(self, region: str) -> List[str]:
        raise NotImplementedError

    def get_cdn_address(self) -> str:
        raise NotImplementedError


"""
When this system was designed, maybe the system only required CloudProvider
to provide services to store and retrive files. So client designed a interface
with store and get method and implemented Amazon and Dropbox.
As program gets larger and added with functionality, it was realized that
we may now need to create servers and use CDN too. But dropbox didn't provided these
services. And theoritically storing data and creating server are two different
domain things. This will eventually create bug in code.
"""


class CloudStorageProvider(Protocol):
    def store_file(self, name: str) -> bool:
        ...

    def get_file(self, name: str) -> bytes:
        ...


class CloudHostingProvider(Protocol):
    def create_server(self, region: str) -> Any:
        ...

    def list_servers(self, region: str) -> List[str]:
        ...


class CDNProvider(Protocol):
    def get_cdn_address(self) -> str:
        ...


@dataclass
class Amazon:
    def store_file(self, name: str) -> bool:
        """stores file in s3"""

    def get_file(self, name: str) -> bytes:
        """get file from s3"""

    def create_server(self, region: str) -> Any:
        """creates ec2 instance"""

    def list_servers(self, region: str) -> List[str]:
        """list ec2 instance"""

    def get_cdn_address(self) -> str:
        """get cdn server url"""


@dataclass
class DropBox:
    def store_file(self, name: str) -> bool:
        """stores file in dropbox"""

    def get_file(self, name: str) -> bytes:
        """get file from dropbox"""


"""
This principle focuses on segregation of interface so that
a class only implements certain inteface to its full. Since DropBox
now does not implement CloudHostingProvider or CDNProvider we now
cannot pass DropBox instance to functions that use these object to create
server or get CDN.
"""
