import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod
from app.books import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonBookSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, book: Book) -> str:
        return json.dumps(
            {"title": self.book.title, "content": self.book.content}
        )


class XmlBookSerializer(BookSerializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")
