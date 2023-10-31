from abc import ABC, abstractmethod
import xml.etree.ElementTree as ElementTree
import json

from app.book import Book


class Serialize(ABC):
    @staticmethod
    @abstractmethod
    def exec(book: Book) -> str:
        pass


class SerializeJson(Serialize):
    @staticmethod
    def exec(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Serialize):
    @staticmethod
    def exec(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


serialize_handlers = {
    "json": SerializeJson(),
    "xml": SerializeXml()
}
