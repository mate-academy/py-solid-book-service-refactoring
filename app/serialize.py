import json
import xml.etree.ElementTree as ElTree

from .book import Book


class BookSerialize:
    def json(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    def xml(self, book: Book) -> str:
        root = ElTree.Element("book")
        title = ElTree.SubElement(root, "title")
        title.text = book.title
        content = ElTree.SubElement(root, "content")
        content.text = book.content
        return ElTree.tostring(root, encoding="unicode")
