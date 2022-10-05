from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Document(ABC):
    data: bytes
    filename: str

    @abstractmethod
    def open(self):
        ...

    @abstractmethod
    def save(self):
        ...


class ReadOnlyDocument(Document):
    def open(self):
        ...


@dataclass
class Project:
    documents: List[Document]

    def open_all(self):
        return [doc.open() for doc in self.documents]

    def save_all(self):
        return [doc.save() for doc in self.documents]


"""
In the design, we can see that ReadOnlyDocument inherit from Document.
But ReadOnlyDocument does not implements save method, as ReadOnlyDocument
as the name suggests only reads the document. This will create issue in our
application as ReadOnlyDocument does not implment all the base classes.
One another thing is that the statistical analysis tool will pass ReadOnlyDocument
call save method as we define typing for all document as Document.
"""


@dataclass
class Document(ABC):
    data: bytes
    filename: str

    def open(self):
        """Open implementation is almost same"""
        ...


class WritableDocument(Document):
    def save(self):
        """Only reimplement save for writable documents"""
        ...


@dataclass
class Project:
    all_docs: List[Document]
    writable_docs: List[WritableDocument]

    def open_all(self):
        return [doc.open() for doc in self.all_docs]

    def save_all(self):
        return [doc.save() for doc in self.writable_docs]


"""
Now in this new approach, the base class Document only defines methods
that will be common to all the child class for that system. i.e. all types
of document either be writable, read-only, etc. must/will have open method.
"""
