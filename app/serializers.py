import json
import xml.etree.ElementTree as Etree
from app.models import Book


class BaseSerializer:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError


class JsonSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BaseSerializer):
    def serialize(self, book: Book) -> str:
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content
        return Etree.tostring(root, encoding="unicode")


class BookSerializer:
    _strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        strategy = BookSerializer._strategies.get(serialize_type)
        if not strategy:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(book)
