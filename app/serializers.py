import json
import xml.etree.ElementTree as ET # noqa
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        ...


class JsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
