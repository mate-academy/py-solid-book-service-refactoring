from app.displayers import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer
from app.book import Book


DISPLAY_METHODS = {"reverse": ReverseDisplay(), "console": ConsoleDisplay()}

PRINT_METHODS = {"console": ConsolePrint(), "reverse": ReversePrint()}

SERIALIZE_METHODS = {"xml": XmlSerializer(), "json": JsonSerializer()}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_METHODS.get(method_type)
            if strategy:
                book.display(strategy)
            else:
                raise ValueError(f"Unknown display method: {method_type}")

        elif cmd == "print":
            strategy = PRINT_METHODS.get(method_type)
            if strategy:
                book.print_book(strategy)
            else:
                raise ValueError(f"Unknown print method: {method_type}")

        elif cmd == "serialize":
            strategy = SERIALIZE_METHODS.get(method_type)
            if strategy:
                return book.serialize(strategy)
            else:
                raise ValueError(f"Unknown serialize method: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
