import json
from xml.etree.ElementTree import Element, SubElement, tostring
from abc import ABC, abstractmethod
from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = Element("book")
        SubElement(root, "title").text = book.title
        SubElement(root, "content").text = book.content
        return tostring(root, encoding="unicode")
