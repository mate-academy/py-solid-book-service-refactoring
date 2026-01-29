import xml.etree.ElementTree as ElementTree

from app.contracts import BookProtocol
from app.serialization.base import Serializer


class XmlSerializer(Serializer):
    def serialize(self, book: BookProtocol) -> str:
        root = ElementTree.Element("book")

        title = ElementTree.SubElement(root, "title")
        title.text = book.title

        content = ElementTree.SubElement(root, "content")
        content.text = book.content

        return ElementTree.tostring(root, encoding="unicode")
