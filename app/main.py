from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serialize import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                book.display(ConsoleDisplay())
            elif method_type == "reverse":
                book.display(ReverseDisplay())
        elif cmd == "print":
            if method_type == "console":
                book.print(ConsolePrint())
            elif method_type == "reverse":
                book.print(ReversePrint())
        elif cmd == "serialize":
            if method_type == "json":
                return book.serialize(JsonSerializer())
            elif method_type == "xml":
                return book.serialize(XmlSerializer())


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
