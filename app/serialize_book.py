from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElementTree
from app.book import Book


class SerializeBook(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class SerializeBookToJson(SerializeBook):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeBookToXml(SerializeBook):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
