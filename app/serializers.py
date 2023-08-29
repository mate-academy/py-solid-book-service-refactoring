import json
import xml.etree.ElementTree as ET


class Serialize:
    def serialize(self, title: str, content: str) -> str:
        raise ValueError("Unknown serialize type")


class JsonSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_et = ET.SubElement(root, "title")
        title_et.text = title
        content_et = ET.SubElement(root, "content")
        content_et.text = content
        return ET.tostring(root, encoding="unicode")
