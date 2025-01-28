import json
import xml.etree.ElementTree as Element_Tree

from abc import ABC, abstractmethod
from app.book import Book


class SerializeWay(ABC):
    @abstractmethod
    def serialize_book(self, book: Book) -> str:
        pass


class SerializeJson(SerializeWay):
    def serialize_book(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(SerializeWay):
    def serialize_book(self, book: Book) -> str:
        root = Element_Tree.Element("book")
        title = Element_Tree.SubElement(root, "title")
        title.text = book.title
        content = Element_Tree.SubElement(root, "content")
        content.text = book.content
        return Element_Tree.tostring(root, encoding="unicode")
