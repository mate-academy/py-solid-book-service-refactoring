from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer

Displayers = {
    "console": ConsoleDisplayer,
    "reverse": ReverseDisplayer,
}

Printers = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

Serializers = {
    "xml": XMLSerializer,
    "json": JSONSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = Displayers[method_type]()
            displayer.display(book)
        elif cmd == "print":
            printer = Printers[method_type]()
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = Serializers[method_type]()
            return serializer.serialize(book)

    if __name__ == "__main__":
        sample_book = Book("Sample Book", "This is some sample content.")
        print(main(sample_book, [("display", "reverse"),
                                 ("serialize", "xml")]))
