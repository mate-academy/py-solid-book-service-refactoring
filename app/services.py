import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod
from app.models import Book


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class ConsoleFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class ReverseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[::-1]


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


FORMATTERS = {
    "console": ConsoleFormatter(),
    "reverse": ReverseFormatter()
}
SERIALIZERS = {
    "json": JSONSerializer(),
    "xml": XMLSerializer()
}
