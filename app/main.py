from app.book import Book
from app.display import DisplayReverse, DisplayConsole
from app.print_book import PrintReverse, PrintConsole
from app.serializer import XMLSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    res = None
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                display = DisplayReverse()
                display.display(book)
            else:
                display = DisplayConsole()
                display.display(book)
        elif cmd == "print":
            if method_type == "reverse":
                printer = PrintReverse()
                printer.print_book(book)
            else:
                printer = PrintConsole()
                printer.print_book(book)

        elif cmd == "serialize":
            if method_type == "xml":
                serializer = XMLSerializer()
                res = serializer.serialize(book)
            else:
                serializer = JsonSerializer()
                res = serializer.serialize(book)
    return res


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("display", "reverse"),
                ("serialize", "xml"),
                ("print", "reverse"),
            ],
        )
    )
