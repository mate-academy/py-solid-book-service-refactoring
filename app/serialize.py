import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod
from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeJson(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps(({"title": book.title, "content": book.content}))


class SerializeXml(Serialize):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
