from app.book import Book
from app.display import (
    ReverseDisplay,
    ConsoleDisplay
)
from app.print import (
    ReversePrint,
    ConsolePrint
)
from app.serializer import (
    XMLSerialization,
    JSONSerialization
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                strategy = ReverseDisplay()
            else:
                strategy = ConsoleDisplay()
            book.display(strategy)
        elif cmd == "print":
            if method_type == "reverse":
                strategy = ReversePrint()
            else:
                strategy = ConsolePrint()
            book.print(strategy)
        elif cmd == "serialize":
            if method_type == "xml":
                strategy = XMLSerialization()
            else:
                strategy = JSONSerialization()
            return book.serialize(strategy)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
