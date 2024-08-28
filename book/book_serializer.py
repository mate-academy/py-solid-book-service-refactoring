import json
import xml
import xml.etree.ElementTree as eT

from book.book import Book


class SerializeBook(Book):
    def __init__(self, book: Book) -> None:
        super().__init__(title=book.title, content=book.content)

    def serialize_json(self) -> json:
        return json.dumps({
            "title": self.title,
            "content": self.content
        })

    def serialize_xml(self) -> xml:
        root = eT.Element("book")
        title = eT.SubElement(root, "title")
        title.text = self.title
        content = eT.SubElement(root, "content")
        content.text = self.content
        return eT.tostring(root, encoding="unicode")
