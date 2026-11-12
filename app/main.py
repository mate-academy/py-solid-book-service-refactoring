from typing import Mapping

from app.Commands import (
    Command,
    DisplayCommand,
    PrintCommand,
    SerializeCommand,
)
from app.Displayers import ConsoleDisplayer, Displayer, ReverseDisplayer
from app.Models import Book
from app.Printers import HeaderPrinter, Printer
from app.Serializers import JsonSerializer, Serializer, XmlSerializer


def build_default_commands() -> dict[str, Command]:
    displayers: dict[str, Displayer] = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer(),
    }
    printers: dict[str, Printer] = {
        "console": HeaderPrinter(
            "Printing the book: {title}...", displayers["console"]
        ),
        "reverse": HeaderPrinter(
            "Printing the book in reverse: {title}...", displayers["reverse"]
        ),
    }
    serializers: dict[str, Serializer] = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }
    return {
        "display": DisplayCommand(displayers),
        "print": PrintCommand(printers),
        "serialize": SerializeCommand(serializers),
    }


def main(
        book: Book,
        commands: list[tuple[str, str]],
        handlers: Mapping[str, Command] | None = None,
) -> None | str:
    handlers = handlers if handlers is not None else build_default_commands()
    for cmd, method_type in commands:
        handler = handlers.get(cmd)
        if handler is None:
            continue  # невідомі команди ігноруються
        result = handler.execute(book, method_type)
        if result is not None:
            return result
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
