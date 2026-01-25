from .book import Book
from .serializers import JsonSerializer, XmlSerializer
from .displayers import ConsoleDisplayer, ReverseDisplayer
from .printers import ConsolePrinter, ReversePrinter


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer()
    }
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    }
    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            displayers[method_type].display(book.content)
        elif cmd == "print":
            printers[method_type].print_book(book)
        elif cmd == "serialize":
            result = serializers[method_type].serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
