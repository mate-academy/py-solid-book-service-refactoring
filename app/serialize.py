import json
import xml.etree.ElementTree as ElementTree
from app.book import Book


class SerializeStrategy:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError("Serialize method it not implemented yet")


class JSONSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializeStrategy(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
