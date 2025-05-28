import json
import xml.etree.ElementTree as ET
from typing import Type, Dict
from app.models import Book


class ISerializer:
    def serialize(self, book: Book) -> str:
        raise NotImplementedError


class JsonSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class SerializerRegistry:
    _serializers: Dict[str, Type[ISerializer]] = {}

    @classmethod
    def register(cls, name: str, serializer_cls: Type[ISerializer]) -> None:
        cls._serializers[name] = serializer_cls

    @classmethod
    def get_serializer(cls, name: str) -> ISerializer:
        serializer_cls = cls._serializers.get(name)
        if not serializer_cls:
            raise ValueError(f"Unknown serialize type: {name}")
        return serializer_cls()


SerializerRegistry.register("json", JsonSerializer)
SerializerRegistry.register("xml", XmlSerializer)
