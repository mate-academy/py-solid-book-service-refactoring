from app.book import Book
from app.book_display import ConsoleDisplay, ReverseDisplay
from app.book_printer import ConsolePrinter, ReversePrinter
from app.book_serializer import JsonSerializer, XMLSerializer



def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }
    printers = {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,
    }
    serializers = {
        "xml": XMLSerializer,
        "json": JsonSerializer,
    }
    for cmd, method_type in commands:
        if cmd == "display":
            display = displayers[method_type]()
            display.display(book)
        elif cmd == "print":
            printer = printers[method_type]()
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = serializers[method_type]()
            return serializer.serialize(book)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
