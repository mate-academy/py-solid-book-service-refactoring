import json
from xml.etree import ElementTree as ElT
from abc import ABC, abstractmethod

from app.book import Book


class BaseSerializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> str:
        pass


class JSONSerializer(BaseSerializer):
    def serialize(self) -> str:
        return json.dumps({"title": self.book.title,
                           "content": self.book.content})


class XMLSerializer(BaseSerializer):
    def serialize(self) -> str:
        root = ElT.Element("book")
        title = ElT.SubElement(root, "title")
        title.text = self.book.title
        content = ElT.SubElement(root, "content")
        content.text = self.book.content
        return ElT.tostring(root, encoding="unicode")
