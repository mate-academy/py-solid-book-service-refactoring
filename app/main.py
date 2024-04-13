from app.book import Book
from app.book_displayers import ReverseDisplay, ConsoleDisplay
from app.book_printers import ConsolePrinter, ReversePrinter
from app.book_serializers import JsonSerializer, XmlSerializer


COMMANDS = {
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
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy = COMMANDS.get("display").get(method_type)
            display_strategy(book).display()
        elif cmd == "print":
            printer_strategy = COMMANDS.get("print").get(method_type)
            printer_strategy(book).print_book()
        elif cmd == "serialize":
            serializer_strategy = COMMANDS.get("serialize").get(method_type)
            return serializer_strategy(book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
