from .models import Book
from .displayers import BookDisplayer, ConsoleDisplayer, ReverseDisplayer
from .printers import BookPrinter, ConsolePrinter, ReversePrinter
from .serializers import BookSerializer, JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer: BookDisplayer
            if method_type == "console":
                displayer = ConsoleDisplayer()
            elif method_type == "reverse":
                displayer = ReverseDisplayer()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            displayer.display(book)

        elif cmd == "print":
            printer: BookPrinter
            if method_type == "console":
                printer = ConsolePrinter()
            elif method_type == "reverse":
                printer = ReversePrinter()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            printer.print_book(book)

        elif cmd == "serialize":
            serializer: BookSerializer
            if method_type == "json":
                serializer = JsonSerializer()
            elif method_type == "xml":
                serializer = XmlSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)
