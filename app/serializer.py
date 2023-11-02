import abc
import json
import xml.etree.ElementTree as ElementTree

from app.book import Book


class SerializeBook(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def serialize(book: Book) -> str:
        pass


class SerializeJson(SerializeBook):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(SerializeBook):
    @staticmethod
    def serialize(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
