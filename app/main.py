from app.models import Book
from app.services import BookPrinter
from app.strategies.output import ConsoleOutput, ReverseOutput
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    strategies = {
        "console": ConsoleOutput(),
        "reverse": ReverseOutput(),
    }
    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            BookPrinter.display(book, strategies[method_type])
        elif cmd == "print":
            BookPrinter.print_book(book, strategies[method_type])
        elif cmd == "serialize":
            result = serializers[method_type].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
