from abc import ABC, abstractmethod

from app.models import (
    Book,
    Display,
    AbstractPrinter,
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrinter,
    ReversePrinter
)
from app.serializers import (
    AbstractSerializer,
    JSONSerializer,
    XMLSerializer
)


class Action(ABC):
    @abstractmethod
    def execute(self, book: Book, mode: str) -> None | str:
        pass


class DisplayAction(Action):
    def __init__(self, displayers: dict[str, Display]) -> None:
        self.displayers = displayers

    def execute(self, book: Book, mode: str) -> None:
        self.displayers[mode].display(book)


class PrintAction(Action):
    def __init__(self, printers: dict[str, AbstractPrinter]) -> None:
        self.printers = printers

    def execute(self, book: Book, mode: str) -> None:
        self.printers[mode].print_book(book)


class SerializerAction(Action):
    def __init__(self, serializers: dict[str, AbstractSerializer]) -> None:
        self.serializers = serializers

    def execute(self, book: Book, mode: str) -> str:
        return self.serializers[mode].serialize(book)


ACTIONS = {
    "display": DisplayAction(
        displayers={
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay()
        }
    ),
    "print": PrintAction(
        printers={
            "console": ConsolePrinter(),
            "reverse": ReversePrinter()
        }
    ),
    "serialize": SerializerAction(
        serializers={
            "json": JSONSerializer(),
            "xml": XMLSerializer()
        }
    ),
}
