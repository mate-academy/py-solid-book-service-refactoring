from app.book import Book
from app.service.display import ConsoleDisplay, ReverseDisplay
from app.service.printer import ConsolePrinter, ReversePrinter
from app.service.serializer import XMLSerializer, JSONSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    }
    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            displays[method_type].display(book.content)
        elif cmd == "print":
            printers[method_type].print_book(book.title, book.content)
        elif cmd == "serialize":
            return serializers[method_type].serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
