import json
import xml.etree.ElementTree as Et

from app.interfaces import Serializer


class JsonSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        root = Et.Element("book")
        title_element = Et.SubElement(root, "title")
        title_element.text = title
        content_element = Et.SubElement(root, "content")
        content_element.text = content
        return Et.tostring(root, encoding="unicode")
