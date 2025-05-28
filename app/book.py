from .display import ConsoleDisplay, ReverseDisplay
from .printer import ConsolePrint, ReversePrint
from .serializer import JsonSerializer, XmlSerializer

class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

        self.display_strategies = {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        }
        self.print_strategies = {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        }
        self.serialize_strategies = {
            "json": JsonSerializer(),
            "xml": XmlSerializer(),
        }

    def display(self, display_type: str) -> None:
        strategy = self.display_strategies.get(display_type)
        if not strategy:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(self.content)

    def print_book(self, print_type: str) -> None:
        strategy = self.print_strategies.get(print_type)
        if not strategy:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print_book(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        strategy = self.serialize_strategies.get(serialize_type)
        if not strategy:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(self.title, self.content)
