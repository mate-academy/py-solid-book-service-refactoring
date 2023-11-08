import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize_book(self, book: Book) -> None:
        pass


class SerializeToJSON(Serialize):
    def serialize_book(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeToXML(Serialize):
    def serialize_book(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
