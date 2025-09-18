from .book import Book
import json
import xml.etree.ElementTree as eT
from abc import ABC, abstractmethod


class BookSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class BookJSONSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> json:
        return json.dumps({"title": book.title, "content": book.content})


class BookXMLSerializer(BookSerializer):
    @staticmethod
    def serialize(book: Book) -> eT:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = book.title
        content = eT.SubElement(root, "content")
        content.text = book.content
        return eT.tostring(root, encoding="unicode")
