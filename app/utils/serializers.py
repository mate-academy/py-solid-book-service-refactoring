import json
import xml.etree.ElementTree as eT

from app.utils.handlers import Serialize


class JsonSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        root = eT.Element("book")
        title_element = eT.SubElement(root, "title")
        title_element.text = title
        content_element = eT.SubElement(root, "content")
        content_element.text = content
        return eT.tostring(root, encoding="unicode")
