import json
import xml.etree.ElementTree as ET  # noqa: N817
from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JSONSerializer(Serializer):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerializer(Serializer):
    _ENCODING_TYPE = "unicode"

    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        root_title = ET.SubElement(root, "title")
        root_title.text = title
        root_content = ET.SubElement(root, "content")
        root_content.text = content
        return ET.tostring(root, encoding=self._ENCODING_TYPE)


class SerializeCMD:
    __SERIALIZE_TYPES = {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }

    @classmethod
    def serialize(cls, serialize_type: str, book: object) -> str:
        serializer = cls.__SERIALIZE_TYPES.get(serialize_type)
        if serializer:
            return serializer.serialize(book.title, book.content)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
