import json
import xml.etree.ElementTree as et  # noqa: N813
from app.models import Book


class JsonSerializer:
    """Serializes a Book object into JSON format."""
    def serialize(self, book: Book) -> str:
        """Return the JSON representation of the book."""
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer:
    """Serializes a Book object into XML format."""
    def serialize(self, book: Book) -> str:
        """Return the XML representation of the book."""
        root = et.Element("book")
        title = et.SubElement(root, "title")
        title.text = book.title
        content = et.SubElement(root, "content")
        content.text = book.content
        return et.tostring(root, encoding="unicode")
