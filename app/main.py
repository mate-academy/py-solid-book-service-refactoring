from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.models import Book
from app.serializer import XmlSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    print_strategies = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategies[method_type].display(book)
        elif cmd == "print":
            print_strategies[method_type].print_book(book)
        elif cmd == "serialize":
            return serializers[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
