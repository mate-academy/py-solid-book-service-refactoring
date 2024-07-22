import json
import xml.etree.ElementTree as ET  # NOQA N817


class Display:
    @staticmethod
    def console(content: str) -> None:
        print(content)

    @staticmethod
    def reverse(content: str) -> None:
        print(content[::-1])


class Print:
    @staticmethod
    def console(title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)

    @staticmethod
    def reverse(title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class Serialize:
    @staticmethod
    def json(title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})

    @staticmethod
    def xml(title: str, content: str) -> str:
        root = ET.Element("book")
        et_title = ET.SubElement(root, "title")
        et_title.text = title
        et_content = ET.SubElement(root, "content")
        et_content.text = content
        return ET.tostring(root, encoding="unicode")
