import json
import xml.etree.ElementTree as Et


class Serialize:
    def serialize(self, title: str, content: str) -> str:
        raise ValueError("Unknown serialize type")


class JsonSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        root = Et.Element("book")
        title_element = Et.SubElement(root, "title")
        title_element.text = title
        content_element = Et.SubElement(root, "content")
        content_element.text = content
        return Et.tostring(root, encoding="unicode")
