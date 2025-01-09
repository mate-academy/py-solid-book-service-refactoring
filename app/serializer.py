import json
import xml.etree.ElementTree as ET

from app.book import Book
from app.command_execute import CommandExecute


class JSONSerializer(CommandExecute):
    def __init__(self, book: Book) -> None:
        self.book = book

    def execute(self) -> str:
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XMLSerializer(CommandExecute):
    def __init__(self, book: Book) -> None:
        self.book = book

    def execute(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content

        return ET.tostring(root, encoding="unicode")
