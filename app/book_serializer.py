import json
import xml.etree.ElementTree as ElTr
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONBookSerializer(BookSerializer):

    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XMLBookSerializer(BookSerializer):

    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = ElTr.Element("book")
        title = ElTr.SubElement(root, "title")
        title.text = self.book.title
        content = ElTr.SubElement(root, "content")
        content.text = self.book.content
        return ElTr.tostring(root, encoding="unicode")
