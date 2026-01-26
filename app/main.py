from typing import List, Tuple, Optional
from app.book import Book
from app.service import BookService
from app.io_handlers import ConsoleWriter
from app.strategies import (
    ConsoleDisplay, ReverseDisplay,
    ConsolePrinter, ReversePrinter,
    JsonSerializer, XmlSerializer
)


def main(book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
    writer = ConsoleWriter()

    display_strategies = {
        "console": ConsoleDisplay(writer),
        "reverse": ReverseDisplay(writer)
    }

    print_strategies = {
        "console": ConsolePrinter(writer),
        "reverse": ReversePrinter(writer)
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    service = BookService(
        display_strategies=display_strategies,
        print_strategies=print_strategies,
        serialize_strategies=serialize_strategies
    )

    return service.process(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book",
                       "This is some sample content.")
    print(main(sample_book,
               [("display", "reverse"), ("serialize", "xml")]))
