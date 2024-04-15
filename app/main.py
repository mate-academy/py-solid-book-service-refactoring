from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer

methods = {
    "display": {"console": ConsoleDisplay, "reverse": ReverseDisplay},
    "print": {"console": ConsolePrinter, "reverse": ReversePrinter},
    "serialize": {"json": JsonSerializer, "xml": XmlSerializer}
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    for cmd, method_type in commands:
        if cmd == "display":
            display_action = methods.get("display").get(method_type)
            display_action(book).display()
        elif printer_action := methods.get("print").get(method_type):
            printer_action(book).print_book()
        elif serialize_action := methods.get("serialize").get(method_type):
            return serialize_action(book).serialize()
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
