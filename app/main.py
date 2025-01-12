from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import XmlSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display = ConsoleDisplay(book)
            elif method_type == "reverse":
                display = ReverseDisplay(book)
            display.display()
        elif cmd == "print":
            if method_type == "console":
                printer = ConsolePrinter(book)
            elif method_type == "reverse":
                printer = ReversePrinter(book)
            printer.print_book()
        elif cmd == "serialize":
            if method_type == "xml":
                serializer = XmlSerializer(book)
            elif method_type == "json":
                serializer = JsonSerializer(book)
            return serializer.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
