from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = {
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay(),
            }.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)

        elif cmd == "print":
            strategy = {
                "console": ConsolePrint(),
                "reverse": ReversePrint(),
            }.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book)

        elif cmd == "serialize":
            strategy = {
                "json": JsonSerializer(),
                "xml": XmlSerializer(),
            }.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return strategy.serialize(book)
