from abc import ABC, abstractmethod
import json
from xml.etree import ElementTree

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps(
            {"title": book.title, "content": book.content}
        )


class XMLSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        ElementTree.SubElement(root, "title").text = book.title
        ElementTree.SubElement(root, "content").text = book.content
        return ElementTree.tostring(root, encoding="unicode")
