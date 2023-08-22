import json
from abc import ABC
import xml.etree.ElementTree as ElementTree


class BookSerialize(ABC):
    def serialize(self, title: str, content: str) -> str:
        raise ValueError("Unknown serialize type")


class BookSerializeJSON(BookSerialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class BookSerializeXML(BookSerialize):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content
        return ElementTree.tostring(root, encoding="unicode")
