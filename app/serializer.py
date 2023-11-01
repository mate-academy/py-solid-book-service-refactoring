import json
import xml.etree.ElementTree as Et

from app.book import Book


class SerializeJson:
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize_json(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml:
    def __init__(self, serialize_type: str) -> None:
        self.serialize_type = serialize_type

    def serialize_xml(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
