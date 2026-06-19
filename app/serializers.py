import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


class SerializationManager:
    _serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    @classmethod
    def serialize(cls, book: Book, serialize_type: str) -> str:
        serializer = cls._serializers.get(serialize_type)
        if not serializer:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return serializer.serialize(book)
