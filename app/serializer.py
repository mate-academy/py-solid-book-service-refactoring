import json
import xml.etree.ElementTree as ET


class Serializer:
    def __init__(self, book):
        self.book = book

    def json_serialize(self):
        return json.dumps({"title": self.book.title, "content": self.book.content})

    def xml_serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")

    def serialize(self, method_type: str):
        method_name = f"{method_type}_serialize"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown serialize method: {method_type}")

        return method()
