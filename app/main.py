from app.book import Book
from app.display import ConsoleDisplayer, ReverseDisplayer
from app.print import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplayer.display(book)
            elif method_type == "reverse":
                ReverseDisplayer.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                ConsolePrinter.print_book(book)
            elif method_type == "reverse":
                ReversePrinter.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerializer.serialize(book)
            elif method_type == "xml":
                return XmlSerializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
        else:
            raise ValueError(f"Unknown cmd command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("serialize", "json")]))
