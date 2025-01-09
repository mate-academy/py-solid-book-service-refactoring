from typing import List, Tuple
from app.book import Book
from app.book_service import BookService
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_strategy import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: List[Tuple[str, str]]) -> None | str:
    service = BookService(book)

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                service.execute_display(ConsoleDisplay())
            elif method_type == "reverse":
                service.execute_display(ReverseDisplay())
        elif cmd == "print":
            if method_type == "console":
                service.execute_print(ConsolePrint())
            elif method_type == "reverse":
                service.execute_print(ReversePrint())
        elif cmd == "serialize":
            if method_type == "json":
                return service.execute_serialize(JsonSerializer())
            elif method_type == "xml":
                return service.execute_serialize(XmlSerializer())


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
