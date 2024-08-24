import json
import xml.etree.ElementTree as ET

from abc import abstractmethod, ABC


class BookSerialize(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> any:
        pass


class BookSerializeJson(BookSerialize):
    def serialize(self, title: str, content: str) -> any:
        return json.dumps({
            "title": title,
            "content": content
        })


class BookSerializeXML(BookSerialize):
    def serialize(self, title: str, content: str) -> any:
        root = ET.Element("book")
        title_el = ET.SubElement(root, "title")
        title_el.text = title
        content_el = ET.SubElement(root, "content")
        content_el.text = content
        return ET.tostring(root, encoding="unicode")
