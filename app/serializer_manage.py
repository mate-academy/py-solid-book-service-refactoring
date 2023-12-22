import json
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod
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
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
