import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book import Book


class BookSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class BookJSONSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookXMLSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> ElementTree:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
