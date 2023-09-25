import json
import xml.etree.ElementTree as Et

from app.book import Book


class Serializer:
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")


class SerializerFactory:
    @staticmethod
    def get_serializer(serialize_type: str) -> Serializer:
        if serialize_type == "json":
            return JsonSerializer()
        if serialize_type == "xml":
            return XmlSerializer()
        raise ValueError(f"Unknown serialize type: {serialize_type}")
