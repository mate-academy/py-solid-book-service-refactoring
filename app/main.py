from app.book import Book, BookDisplayer, BookPrinter, BookSerializer
from app.displayer import ConsoleDisplayer, ReverseDisplayer
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None:
    serializer = BookSerializer(book, {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    })

    printer = BookPrinter(book, {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    })

    displayer = BookDisplayer(book, {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer()
    })

    for cmd, method_type in commands:
        if cmd == "display":
            displayer.display(method_type)
        elif cmd == "print":
            printer.print_book(method_type)
        elif cmd == "serialize":
            return serializer.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
