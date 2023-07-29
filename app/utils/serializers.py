from abc import ABC, abstractmethod


class Serialize(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        import json
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        import xml.etree.ElementTree as ElementTree
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content
        return ElementTree.tostring(root, encoding="unicode")
