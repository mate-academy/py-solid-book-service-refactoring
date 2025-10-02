from app.book import Book
from app.display_strategies import ConsoleDisplay, ReverseDisplay
from app.print_strategies import ConsolePrinter, ReversePrinter
from app.serialize_strategies import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }
    print_strategies = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    }
    serialize_strategies = {
        "json": JSONSerializer(),
        "xml": XMLSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display = display_strategies.get(method_type)
            if not display:
                raise ValueError(f"Unknown display type: {method_type}")
            display.display(book.content)
        elif cmd == "print":
            printer = print_strategies.get(method_type)
            if not printer:
                raise ValueError(f"Unknown print type: {method_type}")
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = serialize_strategies.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
