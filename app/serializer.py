import json
import xml.etree.ElementTree as ElementTree
from app.models import Book


class JSONBookSerializer:
    def serialize(self: Book) -> str:
        return json.dumps(
            {
                "title": self.title,
                "content": self.content
            }
        )


class XMLBookSerializer:
    def serialize(self: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content
        return ElementTree.tostring(root, encoding="unicode")
