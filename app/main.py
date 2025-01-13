from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.models import Book
from app.printers import ConsolePrinter, Printer, ReversePrinter
from app.serializers import JsonSerializer, Serializer, XmlSerializer

from app.displayers import Displayer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = get_displayer(method_type)
            displayer.display(book.content)
        elif cmd == "print":
            printer = get_printer(method_type)
            printer.print(book.title, book.content)
        elif cmd == "serialize":
            serializer = get_serializer(method_type)
            return serializer.serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


def get_displayer(method_type: str) -> Displayer:
    if method_type == "console":
        return ConsoleDisplayer()
    elif method_type == "reverse":
        return ReverseDisplayer()
    else:
        raise ValueError(f"Unknown display type: {method_type}")


def get_printer(method_type: str) -> Printer:
    if method_type == "console":
        return ConsolePrinter()
    elif method_type == "reverse":
        return ReversePrinter()
    else:
        raise ValueError(f"Unknown print type: {method_type}")


def get_serializer(method_type: str) -> Serializer:
    if method_type == "json":
        return JsonSerializer()
    elif method_type == "xml":
        return XmlSerializer()
    else:
        raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result:
        print(result)
