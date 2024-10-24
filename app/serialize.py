import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree


class SerializeContent(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class SerializeJson(SerializeContent):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class SerializeXml(SerializeContent):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content
        return ElementTree.tostring(root, encoding="unicode")


def get_serialize_class(method_type: str) -> SerializeContent:
    if method_type == "json":
        return SerializeJson()
    elif method_type == "xml":
        return SerializeXml()
    else:
        raise ValueError(f"Unknown serialize method {method_type}")
