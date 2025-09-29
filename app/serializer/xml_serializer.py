import xml.etree.ElementTree as ElementTree
from app.serializer.base import SerializerStrategy
from app.models import Book


class XmlSerializer(SerializerStrategy):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
