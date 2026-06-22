from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


DISPLAYERS = {
    "console": ConsoleDisplayer(),
    "reverse": ReverseDisplayer(),
}

PRINTERS = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = DISPLAYERS.get(method_type)
            if not displayer:
                raise ValueError(f"Unknown display type: {method_type}")
            displayer.display(book)

        elif cmd == "print":
            printer = PRINTERS.get(method_type)
            if not printer:
                raise ValueError(f"Unknown print type: {method_type}")
            printer.print_book(book)

        elif cmd == "serialize":
            serializer = SERIALIZERS.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
