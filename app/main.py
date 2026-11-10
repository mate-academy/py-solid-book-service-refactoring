from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer
from app.service import BookService


def main(
    book: Book,
    commands: list[tuple[str, str]],
    service: BookService | None = None
) -> None | str:
    if service is None:
        service = BookService(
            displays={
                "console": ConsoleDisplay(),
                "reverse": ReverseDisplay()
            },
            printers={
                "console": ConsolePrinter(),
                "reverse": ReversePrinter()
            },
            serializers={
                "json": JsonSerializer(),
                "xml": XmlSerializer()
            }
        )

    for command, method_type in commands:
        if command == "display":
            service.display(book, method_type)
        elif command == "print":
            service.print_book(book, method_type)
        elif command == "serialize":
            return service.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
