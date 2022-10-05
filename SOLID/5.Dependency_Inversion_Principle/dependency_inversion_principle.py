import requests
from dataclasses import dataclass
from typing import Any, Dict, Protocol


@dataclass
class APIIntegrator:
    url: str
    data: Dict[str, Any]

    def get(self) -> str:
        req = requests.get(self.url)
        return req.content.decode()

    def create(self) -> bool:
        req = requests.post(self.url, data=self.data)
        return req.status_code == 201


'''
This principle deals with reversing the dependency. Here, APIIntegrator
class depends on low-level class requests. Suppose in future we may need
to change the library from requests as this may not contain all the
functionality required for the module.
'''

class HTTPClient(Protocol):
    def get(self, url: str) -> str:
        ...

    def post(self, url: str, data: Dict[str, Any]) -> bool:
        ...


class RequestClient:
    def get(self, url: str) -> str:
        req = requests.get(url)
        return req.content.decode()

    def post(self, url: str, data: Dict[str, Any]) -> bool:
        req = requests.post(url, data=data)
        return req.status_code == 201


@dataclass
class APIIntegrator:
    url: str
    data: Dict[str, Any]
    client: HTTPClient

    def get(self) -> str:
        return self.client.get(self.url)

    def create(self) -> bool:
        return self.client.post(self.url, self.data)

'''
Instead of APIIntegrator depend on request library, here the dependency
is inversed. APIIntegrator now depend on HTTPClient which is an abstraction
over request library. Now in future, if we need to change the low-level
class like requests, we just need to change the client in APIIntegrator.
Besides it also support for unit testing APIIntegrator module as for test
we can provide fake client.
'''
import httpx


class HTTPXClient:
    def get(self, url: str) -> str:
        resp = httpx.get(url)
        return resp.text
    
    def post(self, url: str, data: Dict[str, Any]) -> bool:
        resp = httpx.post(url, data=data)
        return resp.status_code == 201


class FakeClient:
    def get(self, url: str) -> str:
        return '''<h1>Hello World</h1>'''

    def post(self, url: str, data: Dict[str, Any]) -> bool:
        return True
