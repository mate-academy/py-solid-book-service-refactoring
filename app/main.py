import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Tuple, List, Dict, Type, Optional


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class IBookAction(ABC):
    @abstractmethod
    def execute(self, book: Book, method_type: str) -> Optional[str]:
        pass


class DisplayAction(IBookAction):
    def execute(self, book: Book, method_type: str) -> None:
        if method_type == "console":
            print(book.content)
        elif method_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {method_type}")


class PrintAction(IBookAction):
    def execute(self, book: Book, method_type: str) -> None:
        if method_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif method_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {method_type}")


class ISerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(ISerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class SerializerRegistry:
    _serializers: Dict[str, Type[ISerializer]] = {}

    @classmethod
    def register(cls, name: str, serializer_cls: Type[ISerializer]) -> None:
        cls._serializers[name] = serializer_cls

    @classmethod
    def get_serializer(cls, name: str) -> ISerializer:
        serializer_cls = cls._serializers.get(name)
        if not serializer_cls:
            raise ValueError(f"Unknown serialize type: {name}")
        return serializer_cls()


SerializerRegistry.register("json", JsonSerializer)
SerializerRegistry.register("xml", XmlSerializer)


class SerializeAction(IBookAction):
    def execute(self, book: Book, method_type: str) -> str:
        serializer = SerializerRegistry.get_serializer(method_type)
        return serializer.serialize(book)


class ActionRegistry:
    _actions: Dict[str, Type[IBookAction]] = {}

    @classmethod
    def register(cls, name: str, action_cls: Type[IBookAction]) -> None:
        cls._actions[name] = action_cls

    @classmethod
    def get_action(cls, name: str) -> IBookAction:
        action_cls = cls._actions.get(name)
        if not action_cls:
            raise ValueError(f"Unknown command: {name}")
        return action_cls()


ActionRegistry.register("display", DisplayAction)
ActionRegistry.register("print", PrintAction)
ActionRegistry.register("serialize", SerializeAction)


def main(book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
    for cmd, method_type in commands:
        action = ActionRegistry.get_action(cmd)
        result = action.execute(book, method_type)
        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
