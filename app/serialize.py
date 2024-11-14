import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeBookJSON(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeBookXML(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
