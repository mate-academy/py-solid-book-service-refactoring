from app.book import Book
from app.displayer import ConsoleDisplayer, ReverseDisplayer
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                displayer = ConsoleDisplayer(book)
            elif method_type == "reverse":
                displayer = ReverseDisplayer(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            displayer.display()

        elif cmd == "print":
            if method_type == "console":
                printer = ConsolePrinter(book)
            elif method_type == "reverse":
                printer = ReversePrinter(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            printer.print()

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JSONSerializer(book)
            elif method_type == "xml":
                serializer = XMLSerializer(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
