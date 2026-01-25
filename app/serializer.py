import xml.etree.ElementTree as eT
import json

from app.interfaces import HasTitleContent


class SerializeStrategy:
    def serialize(self, book: HasTitleContent) -> str:
        raise NotImplementedError


class JsonSerializer(SerializeStrategy):
    def serialize(self, book: HasTitleContent) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(SerializeStrategy):
    def serialize(self, book: HasTitleContent) -> str:
        root = eT.Element("book")

        title = eT.SubElement(root, "title")
        title.text = book.title

        content = eT.SubElement(root, "content")
        content.text = book.content

        return eT.tostring(root, encoding="unicode")
