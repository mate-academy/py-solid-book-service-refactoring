import json
import xml.etree.ElementTree as ElementTree
from app.book import Book


class Serializer:
    cmd_type = "serialize"

    @staticmethod
    def json(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def xml(book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
