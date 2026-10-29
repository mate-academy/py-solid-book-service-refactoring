from app.models.book import Book
from app.services.display_service import (
    DisplayService,
    DisplayStrategyFactory,
)
from app.services.print_service import (
    PrintService,
    PrintStrategyFactory,
)
from app.services.serialize_service import (
    SerializeService,
    SerializeStrategyFactory,
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DisplayStrategyFactory.create(method_type)
            service = DisplayService(strategy)
            service.display(book)
        elif cmd == "print":
            strategy = PrintStrategyFactory.create(method_type)
            service = PrintService(strategy)
            service.print_book(book)
        elif cmd == "serialize":
            strategy = SerializeStrategyFactory.create(method_type)
            service = SerializeService(strategy)
            return service.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
