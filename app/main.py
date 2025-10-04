from app.books import Book
from app.displayers import ConsoleDisplay, ReverseDisplay, BookDisplay
from app.printers import ConsolePrinter, ReversePrinter, BookPrinter
from app.serializers import JsonSerializer, XmlSerializer, BookSerializer


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> None | str | list[str]:

    for cmd, method_type in commands:
        if cmd == "display":

            if method_type == "console":
                display = ConsoleDisplay()
            elif method_type == "reverse":
                display = ReverseDisplay()
            else:
                raise ValueError(f"Unknown method type: {method_type}")
            BookDisplay(display).display_book(book)

        elif cmd == "print":
            if method_type == "console":
                printer = ConsolePrinter()
            elif method_type == "reverse":
                printer = ReversePrinter()
            else:
                raise ValueError(f"Unknown method type: {method_type}")
            BookPrinter(printer).print_book(book)

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JsonSerializer()
            elif method_type == "xml":
                serializer = XmlSerializer()
            else:
                raise ValueError(f"Unknown serializer type: {method_type}")
            return BookSerializer(serializer).serialize_book(book)

        else:
            raise ValueError(f"Unknown command: {cmd}")

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    # print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
    print(main(sample_book, [("display", "reverse")]))
