import json
import xml.etree.ElementTree as ElTree
from abc import ABC, abstractmethod

from app.book import Book


class SerializeBook(ABC):
    serializer_type = ["json", "xml"]

    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> None:
        pass


class JSONSerializer(SerializeBook):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializeBook):
    @staticmethod
    def serialize(book: Book) -> ElTree:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")
