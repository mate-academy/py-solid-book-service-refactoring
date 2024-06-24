import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree
from app.book import Book


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeJson(SerializeBook):
    def serialize(self, book: Book) -> str:
        print("json")
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        print("xml")
        return ElementTree.tostring(root, encoding="unicode")
