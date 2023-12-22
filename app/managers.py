from typing import Any

from .display import DisplayConsole, DisplayReverse
from .print import PrintConsole, PrintReverse
from .serializer import SerializeJson, SerializeXml


class DisplayManager:
    display_managers = {}

    def __init__(self, content: str) -> None:
        self.content = content

        self.display_managers["console"] = DisplayConsole()
        self.display_managers["reverse"] = DisplayReverse()

    def display(self, method_type: str) -> None:
        display_manager = self.display_managers.get(method_type)
        if display_manager:
            display_manager.display(self.content)
        else:
            print(f"Invalid method_type: {method_type}")


class PrintManager:
    print_managers = {}

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

        self.print_managers["console"] = PrintConsole()
        self.print_managers["reverse"] = PrintReverse()

    def print_book(self, method_type: str) -> None:
        print_manager = self.print_managers.get(method_type)
        if print_manager:
            print_manager.print_book(self.title, self.content)
        else:
            print(f"Invalid method_type: {method_type}")


class SerializeManager:
    serialize_managers = {}

    def __init__(self, book: Any) -> None:
        self.book = book

        self.serialize_managers["json"] = SerializeJson()
        self.serialize_managers["xml"] = SerializeXml()

    def serialize(self, method_type: str) -> str:
        serialize_manager = self.serialize_managers.get(method_type)
        if serialize_manager:
            return serialize_manager.serialize(self.book)
        else:
            print(f"Invalid method_type: {method_type}")
