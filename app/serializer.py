from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElTree

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
    def serialize(book: Book) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")
