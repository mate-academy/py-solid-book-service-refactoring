import json
import xml.etree.ElementTree as XmlElementTree
from app.interface import ISerializer


class JSONSerializer(ISerializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(ISerializer):
    def serialize(self, title: str, content: str) -> str:
        root = XmlElementTree.Element("book")
        title_elem = XmlElementTree.SubElement(root, "title")
        title_elem.text = title
        content_elem = XmlElementTree.SubElement(root, "content")
        content_elem.text = content
        return XmlElementTree.tostring(root, encoding="unicode")
