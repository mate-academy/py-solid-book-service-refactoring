import json

import xml.etree.ElementTree as Et

from abc import ABC, abstractmethod


class Serializer(ABC):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @abstractmethod
    def serialize(self) -> str:
        pass


class SerializerJSON(Serializer):

    def serialize(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})


class SerializerXML(Serializer):
    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content
        return Et.tostring(root, encoding="unicode")


class SerializerFactory:
    """
    Factory to create the appropriate Serializer instance
    based on the serialized type.
    """

    @staticmethod
    def serialize(title: str, content: str, serialize_type: str) -> str:
        if serialize_type == "xml":
            return SerializerXML(title=title, content=content).serialize()
        elif serialize_type == "json":
            return SerializerJSON(title=title, content=content).serialize()
        raise ValueError(f"Unknown serialize type: {serialize_type}")
