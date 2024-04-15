import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod

from app.book import Book


class BookSerializer(ABC):

    @abstractmethod
    def serialize_book(self, book: Book) -> None:
        pass


class JsonBookSerializer(BookSerializer):

    def serialize_book(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlBookSerializer(BookSerializer):

    def serialize_book(self, book: Book) -> ElementTree:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


def create_book_serializer(serialize_type: str) -> BookSerializer:

    if serialize_type == "json":
        return JsonBookSerializer()
    elif serialize_type == "xml":
        return XmlBookSerializer()
    raise ValueError(f"Unknown serialize type: {serialize_type}")
