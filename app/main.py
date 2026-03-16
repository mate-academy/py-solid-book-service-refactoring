from app.displays import ConsoleDisplay, ReverseDisplay
from app.models import Book
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import XMLSerializer, JSONSerializer
from app.services import (
    BookCommandService,
    DisplayService,
    PrinterService,
    SerializerService,
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_service = DisplayService(
        displays={
            "reverse": ReverseDisplay(),
            "console": ConsoleDisplay(),
        }
    )
    printer_service = PrinterService(
        printers={
            "reverse": ReversePrinter(),
            "console": ConsolePrinter(),
        }
    )
    serializer_service = SerializerService(
        serializers={
            "xml": XMLSerializer(),
            "json": JSONSerializer(),
        }
    )

    book_service = BookCommandService(
        services={
            "display": display_service,
            "print": printer_service,
            "serialize": serializer_service,
        }
    )
    return book_service.run(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
