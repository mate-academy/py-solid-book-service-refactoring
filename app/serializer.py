import json
from xml.etree.ElementTree import Element, SubElement, tostring
from abc import ABC, abstractmethod

from app.book import Book


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")
