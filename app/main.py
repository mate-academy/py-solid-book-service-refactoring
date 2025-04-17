from app.models import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    display_strategies = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer(),
    }

    print_strategies = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }

    serializer_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            displayer = display_strategies.get(method_type)
            if displayer:
                displayer.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            printer = print_strategies.get(method_type)
            if printer:
                printer.print(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            serializer = serializer_strategies.get(method_type)
            if serializer:
                return serializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
