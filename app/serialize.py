from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ETree


class SerializeInterface(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        raise NotImplementedError


class JsonSerialize(SerializeInterface):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeInterface):
    def serialize(self, book_title: str, book_content: str) -> str:
        root = ETree.Element("book")
        title = ETree.SubElement(root, "title")
        title.text = book_title
        content = ETree.SubElement(root, "content")
        content.text = book_content
        return ETree.tostring(root, encoding="unicode")


class SerializeService:
    allowed_serialize_types = {"json": JsonSerialize, "xml": XmlSerialize}

    def _is_serialize_type_valid(self, serialize_type: str) -> bool:
        return serialize_type in self.allowed_serialize_types

    def handle_serialize(
            self,
            serialize_type: str,
            title: str,
            content: str
    ) -> str:
        if self._is_serialize_type_valid(serialize_type):
            return self.allowed_serialize_types[serialize_type]().serialize(
                title,
                content
            )
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
