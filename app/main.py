from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


DATA = {
    "serialize": {
        "json": JsonSerializer,
        "xml": XmlSerializer,
    },
    "display": {
        "console": ConsoleDisplayer,
        "reverse": ReverseDisplayer,

    },
    "print": {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,

    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        selected_class = DATA[cmd][method_type]

        if cmd == "display":
            selected_class.display(book)

        elif cmd == "print":
            selected_class.print_book(book)

        elif cmd == "serialize":
            return selected_class.serialize_book(book)

        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
