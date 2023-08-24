import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        DisplayCorrectType.get_type(display_type).display(self.content)

    def print_book(self, print_type: str) -> None:
        PrintCorrectType.get_type(print_type).print(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        serialize_strategy = SerializeCorrectType.get_type(serialize_type)
        return serialize_strategy.serialize(self.title, self.content)


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])


class DisplayCorrectType:
    @staticmethod
    def get_type(display_type: str) -> Display:
        if display_type == "console":
            return ConsoleDisplay()
        elif display_type == "reverse":
            return ReverseDisplay()
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class Print(ABC):
    @abstractmethod
    def print(self, title: str, content: str) -> None:
        pass


class ConsolePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(Print):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class PrintCorrectType:
    @staticmethod
    def get_type(print_type: str) -> Print:
        if print_type == "console":
            return ConsolePrint()
        elif print_type == "reverse":
            return ReversePrint()
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class Serialize(ABC):
    @abstractmethod
    def serialize(self, title: str, content: str) -> str:
        pass


class JsonSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XmlSerialize(Serialize):
    def serialize(self, title: str, content: str) -> str:
        root = ElementTree.Element("book")
        title_element = ElementTree.SubElement(root, "title")
        title_element.text = title
        content_element = ElementTree.SubElement(root, "content")
        content_element.text = content
        return ElementTree.tostring(root, encoding="unicode")


class SerializeCorrectType:
    @staticmethod
    def get_type(serialize_type: str) -> Serialize:
        if serialize_type == "json":
            return JsonSerialize()
        elif serialize_type == "xml":
            return XmlSerialize()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
