import json

import xml.etree.ElementTree as Etree
from abc import abstractmethod, ABC

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def execute(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def execute(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def execute(self, book: Book) -> str:
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content
        return Etree.tostring(root, encoding="unicode")
