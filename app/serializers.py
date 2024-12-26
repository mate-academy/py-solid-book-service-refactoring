import json

from xml.etree import ElementTree
from abc import ABC, abstractmethod

from app.objects import Book


class Serializer(ABC):

    @abstractmethod
    def serialize(self) -> str:
        pass


class BookJSONSerializer(Serializer):

    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class BookXMLSerializer(Serializer):

    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")
