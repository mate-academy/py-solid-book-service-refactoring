from typing import Optional
from .entities import Book
from .display import ConsoleDisplay, ReverseDisplay
from .printer import ConsolePrinter, ReversePrinter
from .serializer import JsonSerializer, XmlSerializer
from .commands import CommandProcessor

# Wire default strategies. This can be moved to a DI container if needed.
DEFAULT_DISPLAYS = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

DEFAULT_PRINTERS = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

DEFAULT_SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}

_processor = CommandProcessor(
    displays=DEFAULT_DISPLAYS,
    printers=DEFAULT_PRINTERS,
    serializers=DEFAULT_SERIALIZERS,
)


def main(book: Book, commands: list[tuple[str, str]]) -> Optional[str]:
    """Process commands for a book.

    Behavior preserved:
    - "display" prints content or reversed content to stdout.
    - "print" prints the same header lines and content as before.
    - "serialize" returns JSON/XML exactly as before and stops
      processing further commands.
    - Unknown types raise the same ValueError messages.
    """
    return _processor.run(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
