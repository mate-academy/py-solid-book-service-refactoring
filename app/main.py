from app.display_book import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrinter, ReversePrinter
from app.serializer_book import JsonSerializer, XmlSerializer
from app.book import Book

data = {
    "display": {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    },
    "print": {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,
    },
    "serialize": {
        "json": JsonSerializer,
        "xml": XmlSerializer,
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd not in data or method_type not in data[cmd]:
            print(f"Unknown command or method type: {cmd}, {method_type}")
            continue

        if cmd == "display":
            display_strategy = data[cmd][method_type]()
            print(display_strategy.display(book.content))
        elif cmd == "print":
            printer_strategy = data[cmd][method_type]()
            printer_strategy.print_content(book.title, book.content)
        elif cmd == "serialize":
            serializer_strategy = data[cmd][method_type]()
            return serializer_strategy.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
