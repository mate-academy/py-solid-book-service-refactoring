import json
import xml.etree.ElementTree as Etree
from book.book import Book


class BookSerializer:
    def serialize(self, book: Book) -> str:
        pass


class JSONBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content
        return Etree.tostring(root, encoding="unicode")
