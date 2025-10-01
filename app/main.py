from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay, Printer, ReversePrinter
from app.serialize import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    methods = {
        "display_console": ConsoleDisplay(),
        "display_reverse": ReverseDisplay(),
        "print_console": Printer(),
        "print_reverse": ReversePrinter(),
    }
    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }
    for cmd, method_type in commands:
        if cmd in ("display", "print"):
            method = methods.get(f"{cmd}_{method_type}")
            if method:
                method.display(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if serializer:
                return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
