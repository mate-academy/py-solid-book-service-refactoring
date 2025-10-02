import json
import xml.etree.ElementTree as ElTr
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JsonBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> None:
        root = ElTr.Element("book")
        title = ElTr.SubElement(root, "title")
        title.text = book.title
        content = ElTr.SubElement(root, "content")
        content.text = book.content
        return ElTr.tostring(root, encoding="unicode")
