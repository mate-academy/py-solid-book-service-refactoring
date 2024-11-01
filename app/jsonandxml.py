import json
import xml.etree.ElementTree
from app.serializers import SerializeInterface


class JsonSerializer(SerializeInterface):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerializer(SerializeInterface):
    def serialize(self, title: str, content: str) -> str:
        root = xml.etree.ElementTree.Element("book")
        xml.etree.ElementTree.SubElement(root, "title").text = title
        xml.etree.ElementTree.SubElement(root, "content").text = content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")
