from app.display import ConsoleDisplay, ReverseDisplay
from app.serializer import JsonSerializer, XMLSerializer
from app.print import PrintConsole, PrintReverse
from app.book import Book


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> None | str:

    for cmd, method_type in commands:
        if cmd == "display" and method_type == "console":
            ConsoleDisplay(book).display()
        elif cmd == "display" and method_type == "reverse":
            ReverseDisplay(book).display()
        elif cmd == "print" and method_type == "console":
            PrintConsole(book).print()
        elif cmd == "print" and method_type == "reverse":
            PrintReverse(book).print()
        elif cmd == "serialize" and method_type == "json":
            return JsonSerializer(book).serialize()
        elif cmd == "serialize" and method_type == "xml":
            return XMLSerializer(book).serialize()


if __name__ == "__main__":
    sample_book = Book(
        "Sample Book",
        "This is some sample content."
    )
    print(
        main(sample_book,
             [("display", "reverse"),
              ("serialize", "xml")])
    )
