import json
import xml.etree.ElementTree as et

from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize_book(self) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize_book(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XmlSerializer(Serializer):
    def serialize_book(self) -> str:
        root = et.Element("book")
        title = et.SubElement(root, "title")
        title.text = self.book.title
        content = et.SubElement(root, "content")
        content.text = self.book.content
        return et.tostring(root, encoding="unicode")
