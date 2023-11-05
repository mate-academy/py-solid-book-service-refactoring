import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize_book(
        self,
    ) -> None:
        pass


class SerializeJson(Serialize):
    def __init__(self, book: Book) -> None:
        self.method_type = "json"
        self.title = book.title
        self.content = book.content

    def serialize_book(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXML(Serialize):
    def __init__(self, book: Book) -> None:
        self.method_type = "json"
        self.title = book.title
        self.content = book.content

    def serialize_book(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")
