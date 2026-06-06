from app.book import Book
from app.display import ReverseDisplay, ConsoleDisplay
from app.printer import Printer
from app.serializer import XMLSerializer, JSONSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }

    printer = Printer()
    for cmd, method_type in commands:
        if cmd == "display":
            displays[method_type].display(book.content)
        elif cmd == "print":
            printer.print(displays[method_type], book)
        elif cmd == "serialize":
            return serializers[method_type].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
