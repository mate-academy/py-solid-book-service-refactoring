import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.main import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
