import json
import xml.etree.ElementTree as Et

from abc import ABC, abstractmethod
from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JSONSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
