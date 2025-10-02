from app.models.book import Book
from app.services.book_service import BookService
from app.strategies.display import ConsoleDisplay, ReverseDisplay
from app.strategies.print_book import ConsolePrint, ReversePrint
from app.strategies.serialize import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    service = BookService(book)
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                service.display(ConsoleDisplay())
            elif method_type == "reverse":
                service.display(ReverseDisplay())
        elif cmd == "print":
            if method_type == "console":
                service.print_book(ConsolePrint())
            elif method_type == "reverse":
                service.print_book(ReversePrint())
        elif cmd == "serialize":
            if method_type == "json":
                result = service.serialize(JsonSerialize())
            elif method_type == "xml":
                result = service.serialize(XmlSerialize())
    return result


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")
    service = BookService(book)

    service.display(ReverseDisplay())
    print(service.serialize(XmlSerialize()))
