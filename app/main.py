from app.displayers import (
    ConsoleDisplayer,
    ReverseDisplayer,
    DummyDisplayer
)
from app.printers import (
    ConsolePrinter,
    ReversePrinter,
    DummyPrinter
)
from app.serializers import (
    JsonSerializer,
    XmlSerializer,
    DummySerializer
)
from app.services import BookService
from app.books import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer_map = {
                "console": ConsoleDisplayer(),
                "reverse": ReverseDisplayer(),
            }
            displayer = displayer_map[method_type]
            service = BookService(
                displayer=displayer,
                printer=DummyPrinter(),
                serializer=DummySerializer()
            )
            service.display(book)

        elif cmd == "print":
            printer_map = {
                "console": ConsolePrinter(),
                "reverse": ReversePrinter(),
            }
            printer = printer_map[method_type]
            service = BookService(
                displayer=DummyDisplayer(),
                printer=printer,
                serializer=DummySerializer()
            )
            service.print_book(book)

        elif cmd == "serialize":
            serializer_map = {
                "json": JsonSerializer(),
                "xml": XmlSerializer(),
            }
            serializer = serializer_map[method_type]
            service = BookService(
                displayer=DummyDisplayer(),
                printer=DummyPrinter(),
                serializer=serializer
            )
            return service.serialize(book)

        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
