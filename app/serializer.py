import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as Et
from app.book import ObjectWithContent


class SerializerConstructor(ABC):
    def __init__(
            self,
            serialize_type: str,
            object_to_serialize: ObjectWithContent
    ) -> None:
        self.serialize_type = serialize_type
        self.object_to_serialize = object_to_serialize


class Serializer(SerializerConstructor):
    @abstractmethod
    def serialize(self) -> str:
        pass


class JsonSerializer(Serializer):
    def __init__(self, object_to_serialize: ObjectWithContent) -> None:
        super().__init__("json", object_to_serialize)

    def serialize(self) -> str:
        return json.dumps(
            {
                "title": self.object_to_serialize.title,
                "content": self.object_to_serialize.content
            }
        )


class XmlSerializer(Serializer):
    def __init__(self, object_to_serialize: ObjectWithContent) -> None:
        super().__init__("xml", object_to_serialize)

    def serialize(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.object_to_serialize.title
        content = Et.SubElement(root, "content")
        content.text = self.object_to_serialize.content
        return Et.tostring(root, encoding="unicode")


class SerializerFactory(SerializerConstructor):
    def __init__(
            self,
            serialize_type: str,
            object_to_serialize: ObjectWithContent
    ) -> None:
        super().__init__(
            serialize_type,
            object_to_serialize
        )

    def create_serializer(self) -> Serializer:
        if self.serialize_type == "json":
            return JsonSerializer(self.object_to_serialize)
        elif self.serialize_type == "xml":
            return XmlSerializer(self.object_to_serialize)
