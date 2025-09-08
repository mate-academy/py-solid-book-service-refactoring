from serializer.base import Serializer
from models.book import Book
import xml.etree.ElementTree as ElementTree


class SerializeXML(Serializer):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        ElementTree.SubElement(root, "title").text = book.title
        ElementTree.SubElement(root, "content").text = book.content
        return ElementTree.tostring(root, encoding="unicode")
