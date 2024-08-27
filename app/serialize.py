import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as Et

from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
