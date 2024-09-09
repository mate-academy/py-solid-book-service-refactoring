import json
import xml.etree.ElementTree


class ConsoleDisplay:
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay:
    def display(self, content: str) -> None:
        print(content[::-1])


class ConsolePrint:
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...",
              content,
              sep="\n")


class ReversePrint:
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...",
              content[::-1],
              sep="\n")


class JSONSerialize:
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerialize:
    def serialize(self, title: str, content: str) -> str:
        root = xml.etree.ElementTree.Element("book")
        title_element = xml.etree.ElementTree.SubElement(root, "title")
        title_element.text = title
        content_element = xml.etree.ElementTree.SubElement(root, "content")
        content_element.text = content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")
