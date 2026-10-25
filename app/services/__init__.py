"""Book service - high-level module coordinating views, printers, and
serializers.

Following DIP: depends on abstractions (interfaces and factories), not
concrete classes.
Following SRP: single responsibility - orchestrating book operations.
Following OCP: open for extension via factories, closed for modification.
"""

from app.domain.book import Book
from app.factories import ViewerFactory, PrinterFactory, SerializerFactory


class BookService:
    """Service for performing book operations.

    This class coordinates between different operations without knowing
    the concrete implementations. It depends on factories (abstractions)
    for creating the actual implementations.
    """

    def __init__(
        self,
        viewer_factory: ViewerFactory = ViewerFactory(),
        printer_factory: PrinterFactory = PrinterFactory(),
        serializer_factory: SerializerFactory = SerializerFactory(),
    ) -> None:
        self._viewer_factory = viewer_factory
        self._printer_factory = printer_factory
        self._serializer_factory = serializer_factory

    def display(self, book: Book, viewer_type: str) -> None:
        """Display book using specified viewer type."""
        viewer = self._viewer_factory.create(viewer_type)
        viewer.display(book)

    def print(self, book: Book, printer_type: str) -> None:
        """Print book using specified printer type."""
        printer = self._printer_factory.create(printer_type)
        printer.print_book(book)

    def serialize(self, book: Book, serializer_type: str) -> str:
        """Serialize book using specified serializer type."""
        serializer = self._serializer_factory.create(serializer_type)
        return serializer.serialize(book)

    def execute_commands(
        self, book: Book, commands: list[tuple[str, str]]
    ) -> str | None:
        """Execute a sequence of commands on the book.

        Args:
            book: The book to operate on
            commands: List of (command, type) tuples
                      command: "display", "print", or "serialize"
                      type: viewer/printer/serializer type name

        Returns:
            The result of the last serialize command, or None if no
            serialize command
        """
        last_result = None

        for cmd, method_type in commands:
            if cmd == "display":
                self.display(book, method_type)
            elif cmd == "print":
                self.print(book, method_type)
            elif cmd == "serialize":
                last_result = self.serialize(book, method_type)
            else:
                raise ValueError(f"Unknown command: {cmd}")

        return last_result
