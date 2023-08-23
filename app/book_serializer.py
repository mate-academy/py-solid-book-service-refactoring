from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ElT

from app.book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class BookSerializerJSON(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class BookSerializerXML(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElT.Element("book")
        title = ElT.SubElement(root, "title")
        title.text = book.title
        content = ElT.SubElement(root, "content")
        content.text = book.content
        return ElT.tostring(root, encoding="unicode")


class Serializer:
    serialize_types = {"json": BookSerializerJSON, "xml": BookSerializerXML}

    def serialize_book(self, serialize_type: str, book: Book) -> str:
        if serialize_type in self.serialize_types:
            return self.serialize_types[serialize_type]().serialize(book)
        raise ValueError(f"Unknown serialize type: {serialize_type}")
