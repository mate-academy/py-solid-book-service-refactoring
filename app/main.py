from app.services.book import Book
from app.services.displayers import ConsoleDisplay, ReverseDisplay
from app.services.printers import ConsolePrinter, ReversePrinter
from app.services.serializers import JsonSerializer, XMLSerializer


DEFAULT_SERIALIZER = JsonSerializer()

COMMANDS_MAP = {
    "display": {
        "console": ConsoleDisplay(), "reverse": ReverseDisplay()
    },
    "print": {
        "console": ConsolePrinter(), "reverse": ReversePrinter()
    },
    "serialize": {
        "json": JsonSerializer(), "xml": XMLSerializer()
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:

        if cmd == "display":
            COMMANDS_MAP[cmd][method_type].display(book)

        elif cmd == "print":
            COMMANDS_MAP[cmd][method_type].print_book(book)

        elif cmd == "serialize":
            serializer = COMMANDS_MAP[cmd][method_type]

            return serializer.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
