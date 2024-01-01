from __future__ import annotations

from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrint, ReversePrint
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {"console": ConsoleDisplayer(), "reverse": ReverseDisplayer()}
    printers = {"console": ConsolePrint(), "reverse": ReversePrint()}
    serialize_strategies = {"json": JSONSerializer(), "xml": XMLSerializer()}

    for cmd, method_type in commands:
        if cmd == "display":
            displayer = displayers[method_type]
            displayer.display(book)
        elif cmd == "print":
            printer = printers[method_type]
            printer.print_book(book)
        elif cmd == "serialize":
            serialize_strategy = serialize_strategies[method_type]
            return serialize_strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
