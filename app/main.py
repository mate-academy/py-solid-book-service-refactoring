from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                display_strategy = ConsoleDisplay()
            elif method_type == "reverse":
                display_strategy = ReverseDisplay()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            display_strategy.display(book.content)

        elif cmd == "print":
            if method_type == "console":
                print_strategy = ConsolePrinter()
            elif method_type == "reverse":
                print_strategy = ReversePrinter()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            print_strategy.print_book(book.title, book.content)

        elif cmd == "serialize":
            if method_type == "json":
                serializer = JSONSerializer()
            elif method_type == "xml":
                serializer = XMLSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
