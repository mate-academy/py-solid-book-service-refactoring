import json
from xml.etree import ElementTree
from abc import ABC, abstractmethod


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerializer(BookSerializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({
            "title": title,
            "content": content,
        })


class XmlSerializer(BookSerializer):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")

        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title

        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content

        return ElementTree.tostring(root, encoding="unicode")


SERIALIZE_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}
