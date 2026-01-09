import json
import xml.etree.ElementTree as ET


class SerializerStrategy:
    def serialize(self, book) -> str:
        raise NotImplementedError


class JsonSerializer(SerializerStrategy):
    def serialize(self, book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializerStrategy):
    def serialize(self, book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
