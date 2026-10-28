import json
from abc import ABC, abstractmethod
from xml.etree.ElementTree import Element, SubElement, tostring

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")


SERIALIZE_TYPES: dict[str, BookSerializer] = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}
