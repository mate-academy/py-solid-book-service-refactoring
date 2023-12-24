import json

from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book_implementation import Book


class BookSerialize(ABC):
    @staticmethod
    @abstractmethod
    def serialize_book(book: Book) -> str:
        pass


class JsonBookSerialize(BookSerialize):
    @staticmethod
    def serialize_book(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlBookSerialize(BookSerialize):
    @staticmethod
    def serialize_book(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
