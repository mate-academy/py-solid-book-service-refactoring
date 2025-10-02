from .book import Book
from .book_service import BookService
from .printers import IPrint, ConsolePrint, ReversePrint
from .serializers import ISerializer, JsonSerializer, XmlSerializer
from .displays import IDisplay, ConsoleDisplay, ReverseDisplay


DISPLAY_MAP: dict[str, type[IDisplay]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_MAP: dict[str, type[IPrint]] = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}

SERIALIZE_MAP: dict[str, type[ISerializer]] = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}

COMMAND_MAP: dict[str, dict] = {
    "display": DISPLAY_MAP,
    "print": PRINT_MAP,
    "serialize": SERIALIZE_MAP
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book)

    for cmd, method_type in commands:
        if cmd not in COMMAND_MAP:
            raise ValueError(f"Unknown command type: {cmd}")
        method_mapper = COMMAND_MAP[cmd]
        if method_type not in method_mapper:
            raise ValueError(
                f"Unknown method type: {method_type} in commands: {cmd}"
            )

        command = getattr(service, cmd)
        result = command(method_mapper[method_type]())
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
