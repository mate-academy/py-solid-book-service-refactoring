import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.book.book import Book


class BookSerializer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def serialize(self) -> None:
        pass


class JsonBookSerializer(BookSerializer):

    def serialize(self) -> str:
        return json.dumps({
            "title": self.book.title,
            "content": self.book.content
        })


class XMLBookSerializer(BookSerializer):

    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.book.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.book.content
        return ElementTree.tostring(root, encoding="unicode")


def choose_serialize_type(type_name: str) -> [BookSerializer | ValueError]:
    if type_name == "json":
        return JsonBookSerializer
    elif type_name == "xml":
        return XMLBookSerializer
    else:
        raise ValueError(f"Unknown serialize type: {type_name}")


def serialize_book(book: Book, serialize_type: str) -> str:
    serializer = choose_serialize_type(serialize_type)
    book_serializer = serializer(book)
    return book_serializer.serialize()
