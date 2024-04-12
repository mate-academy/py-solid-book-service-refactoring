import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JSONBookSerializer(BookSerializer):

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):

    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def serialize_factor(book: Book, method_type: str) -> str:
    if method_type == "json":
        serializer = JSONBookSerializer()
        return serializer.serialize(book)
    elif method_type == "xml":
        serializer = XMLBookSerializer()
        return serializer.serialize(book)
    else:
        raise ValueError(f"Unknown serialize type: {method_type}")
