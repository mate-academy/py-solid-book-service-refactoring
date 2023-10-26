import json
import xml.etree.ElementTree as ET
from app.book import Book


class BookSerialize:

    def __init__(self, book: Book) -> None:
        self.book = book

    def to_json(self) -> str:
        return json.dumps({"title": self.book.title, "content": self.book.content})

    def to_xml(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
