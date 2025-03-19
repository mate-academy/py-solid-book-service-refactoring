from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display_book(book)
            elif method_type == "reverse":
                ReverseDisplay().display_book(book)
        elif cmd == "print":
            if method_type == "console":
                ConsolePrint().print_book(book)
            elif method_type == "reverse":
                ReversePrint().print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerializer().serialize_book(book)
            elif method_type == "xml":
                return XmlSerializer().serialize_book(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
