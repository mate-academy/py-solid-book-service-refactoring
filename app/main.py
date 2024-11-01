from app.book import Book
from app.printers import ConsolePrinter, ReversePrinter
from app.displays import ReverseDisplay, ConsoleDisplay
from app.jsonandxml import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "reverse":
                book.display(ReverseDisplay())
            else:
                book.display(ConsoleDisplay())
        elif cmd == "print":
            if method_type == "reverse":
                book.print_book(ReversePrinter())
            else:
                book.print_book(ConsolePrinter())
        elif cmd == "serialize":
            if method_type == "json":
                return book.serialize(JsonSerializer())
            elif method_type == "xml":
                return book.serialize(XmlSerializer())


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
