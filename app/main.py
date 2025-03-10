from app.book import Book
from app.display_service import ConsoleDisplayService, ReverseDisplayService
from app.print_service import ConsolePrintService, ReversePrintService
from app.serialize_service import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplayService().display(book)
            elif method_type == "reverse":
                ReverseDisplayService().display(book)
        elif cmd == "print":
            if method_type == "console":
                ConsolePrintService().print_book(book)
            elif method_type == "reverse":
                ReversePrintService().print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerializer().serialize(book)
            elif method_type == "xml":
                return XmlSerializer().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
