import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree

from app.book import Book


class SerializeProcess(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class SerializeProcessJSON(SerializeProcess):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def serialize(self, book: Book) -> json:
        return json.dumps({self.title: book.title, self.content: book.content})


class SerializeProcessXML(SerializeProcess):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def serialize(self, book: Book) -> ElementTree:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, self.title)
        title.text = book.title
        content = ElementTree.SubElement(root, self.content)
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
