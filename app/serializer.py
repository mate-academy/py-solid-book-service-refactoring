import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializeBook(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONSerializeBook(SerializeBook):
    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class XMLSerializeBook(SerializeBook):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
