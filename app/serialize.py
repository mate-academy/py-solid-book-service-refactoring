import abc

import json
from xml.etree import ElementTree


class Serializer(abc.ABC):
    def __init__(self, content: str, title: str) -> None:
        self.content = content
        self.title = title

    @abc.abstractmethod
    def serialize(self) -> str:
        ...


class SerializerJSON(Serializer):

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializerXML(Serializer):
    def serialize(self) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = self.title
        content = ElementTree.SubElement(root, "content")
        content.text = self.content

        return ElementTree.tostring(root, encoding="unicode")
