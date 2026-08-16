from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serialization import JsonBookSerializer, XmlBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }

    serializers = {
        "json": JsonBookSerializer(),
        "xml": XmlBookSerializer(),
    }

    for command, method_type in commands:
        if command == "display":
            displayers[method_type].display(book)
        elif command == "print":
            printers[method_type].print_book(book)
        elif command == "serialize":
            return serializers[method_type].serialize(book)

        else:
            raise ValueError(f"Unknown command: {command}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
