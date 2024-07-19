import json
from xml.etree import ElementTree

from app.abstract_classes import IBookSerializer
from app.book_model import Book


class JSONBookSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
