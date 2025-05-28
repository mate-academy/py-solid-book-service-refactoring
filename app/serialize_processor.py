import json
import xml.etree.ElementTree as El_Tree
from abc import ABC, abstractmethod

from app.book import Book


class SerializeProcessor(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JSONSerializeProcessor(SerializeProcessor):
    def serialize(self, book: Book) -> None:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializeProcessor(SerializeProcessor):
    def serialize(self, book: Book) -> None:
        root = El_Tree.Element("book")
        title = El_Tree.SubElement(root, "title")
        title.text = book.title
        content = El_Tree.SubElement(root, "content")
        content.text = book.content
        return El_Tree.tostring(root, encoding="unicode")
