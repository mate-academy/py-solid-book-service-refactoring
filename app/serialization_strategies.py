import json
from xml.etree.ElementTree import Element, SubElement, tostring
from app.interfaces import ISerializationStrategy


class JsonSerializer(ISerializationStrategy):
    def serialize(self, data: dict) -> str:
        return json.dumps(data)


class XmlSerializer(ISerializationStrategy):
    def serialize(self, data: dict) -> str:
        root = Element("book")
        title = SubElement(root, "title")
        title.text = data.get("title", "")
        content = SubElement(root, "content")
        content.text = data.get("content", "")
        return tostring(root, encoding="unicode")
