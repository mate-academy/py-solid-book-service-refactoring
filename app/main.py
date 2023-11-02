from app.book import Book
from app.book_display import ConsoleDisplay, ReverseDisplay
from app.book_printer import ConsolePrint, ReversePrint
from app.book_serializer import XmlSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }
    printers = {
        "console": ConsolePrint,
        "reverse": ReversePrint,
    }
    serialization = {
        "json": JsonSerializer,
        "xml": XmlSerializer,
    }

    for cmd, method_type in commands:
        if cmd == "display":
            displays[method_type](book).display()
        elif cmd == "print":
            printers[method_type](book).print()
        elif cmd == "serialize":
            return serialization[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
