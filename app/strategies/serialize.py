import json
from xml.etree import ElementTree

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.book import Book


class SerializeStrategy:
    def serialize(self, book: "Book") -> str:
        raise NotImplementedError


class JSONSerializer(SerializeStrategy):
    def serialize(self, book: "Book") -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: "Book") -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")


serializers = {
    "json": JSONSerializer(),
    "xml": XmlSerializer(),
}
