import json
import xml.etree.ElementTree as Et

from app.interfaces.book_serializer_interface import BookSerializerInterface


class JsonBookSerializer(BookSerializerInterface):
    @staticmethod
    def serialize(book: "Book") -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializerInterface):
    @staticmethod
    def serialize(book: "Book") -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
