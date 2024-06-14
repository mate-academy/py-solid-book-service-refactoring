import json

from abc import ABC, abstractmethod

from xml.etree import ElementTree

from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerialize(Serialize):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XmlSerialize(Serialize):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
