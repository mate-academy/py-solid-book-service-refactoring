import json
import xml.etree.ElementTree as ElementTree


class Serialize:
    def serialize(self, title: str, content: str) -> str:
        raise ValueError("Unknown serialize type")


class JsonSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_et = ElementTree.SubElement(root, "title")
        title_et.text = title
        content_et = ElementTree.SubElement(root, "content")
        content_et.text = content
        return ElementTree.tostring(root, encoding="unicode")