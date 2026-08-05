import json
import xml.etree.ElementTree as ElTree

from app.book_base import BookInitialize


class BookSerialize(BookInitialize):
    """Serialize content book depends on serialize type"""
    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = ElTree.Element("book")
            title = ElTree.SubElement(root, "title")
            title.text = self.title
            content = ElTree.SubElement(root, "content")
            content.text = self.content
            return ElTree.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
