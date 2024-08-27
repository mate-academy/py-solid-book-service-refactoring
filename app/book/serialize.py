import json
import xml.etree.ElementTree as ElT
from abc import ABC, abstractmethod
from app.book.book import Book


class Serialize(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JSONSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerialize(Serialize):
    def serialize(self, book: Book) -> str:
        root = ElT.Element("book")
        title = ElT.SubElement(root, "title")
        title.text = book.title
        content = ElT.SubElement(root, "content")
        content.text = book.content
        return ElT.tostring(root, encoding="unicode")
