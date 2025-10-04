import json
from abc import abstractmethod, ABC
import xml.etree.ElementTree as ETree
from app.books import Book


class Serializer(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):

    def serialize(self, book: Book) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book.title
        content = ETree.SubElement(root, "content")
        content.text = book.content
        return ETree.tostring(root, encoding="unicode")


class BookSerializer:

    def __init__(self, serializer: Serializer) -> None:
        self.serializer = serializer

    def serialize_book(self, book: Book) -> str:
        return self.serializer.serialize(book)
