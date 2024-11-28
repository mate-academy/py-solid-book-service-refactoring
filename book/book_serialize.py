from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as El_Tree
from book.book import Book


class SerializeBook(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializeBookJson(SerializeBook):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeBookXml(SerializeBook):
    def serialize(self, book: Book) -> str:
        root = El_Tree.Element("book")
        title = El_Tree.SubElement(root, "title")
        title.text = book.title
        content = El_Tree.SubElement(root, "content")
        content.text = book.content
        return El_Tree.tostring(root, encoding="unicode")
