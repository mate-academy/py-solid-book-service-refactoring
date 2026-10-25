"""Concrete serializer implementations - following SRP and OCP."""

import json
import xml.etree.ElementTree

from app.domain.book import Book
from app.interfaces import BookSerializer


class JSONBookSerializer(BookSerializer):
    """Serialize book to JSON format."""

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):
    """Serialize book to XML format."""

    def serialize(self, book: Book) -> str:
        root = xml.etree.ElementTree.Element("book")
        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title
        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")
