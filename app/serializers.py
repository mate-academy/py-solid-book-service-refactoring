import json
from xml.etree import ElementTree

from app.models import Book
from abc import ABC, abstractmethod


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class BookJsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookXmlSerializer(BookSerializer):
    def serialize(self, book: "Book") -> str:
        root = ElementTree.Element("book")

        title = ElementTree.SubElement(root, "title")
        title.text = book.title

        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")
