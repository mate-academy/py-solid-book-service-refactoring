import json
from abc import ABC, abstractmethod

from app.models import Book
from xml.etree.ElementTree import Element, SubElement, tostring


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializeBook(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializeBook(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = book.title
        content = SubElement(root, "content")
        content.text = book.content
        return tostring(root, encoding="unicode")
