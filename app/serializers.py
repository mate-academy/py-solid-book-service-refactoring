import json

from xml.etree import ElementTree
from abc import ABC, abstractmethod

from app.models import Book


class BookSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize_book(book: Book) -> None:
        pass


class BookJsonSerializer(BookSerializer):
    @staticmethod
    def serialize_book(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookXmlSerializer(BookSerializer):
    @staticmethod
    def serialize_book(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
