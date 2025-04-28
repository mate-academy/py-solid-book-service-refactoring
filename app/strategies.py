import json
import xml.etree.ElementTree as Talon
from interfaces import DisplayStrategy, PrintStrategy, SerializeStrategy


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class ConsolePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintStrategy):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class JsonSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, title: str, content: str) -> str:
        root = Talon.Element("book")
        title_el = Talon.SubElement(root, "title")
        title_el.text = title
        content_el = Talon.SubElement(root, "content")
        content_el.text = content
        return Talon.tostring(root, encoding="unicode")
