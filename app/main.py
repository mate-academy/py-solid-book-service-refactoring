from app.display_types import ConsoleDisplay, ReverseDisplay
from app.interfaces import (
    DisplayBookInterface,
    PrintBookInterface,
    SerializerBookInterface
)
from app.models import Book
from app.print_book_types import ConsolePrint, ReversePrint
from app.serializer_types import XMLSerializer, JsonSerializer


class BookDisplay:
    @staticmethod
    def display(book: Book, display_instance: DisplayBookInterface) -> None:
        display_instance.display_book(book)


class BookPrint:
    @staticmethod
    def print_book(book: Book, print_instance: PrintBookInterface) -> None:
        print_instance.print_book(book)


class BookSerializer:
    @staticmethod
    def serializer(
            book: Book,
            serialize_instance: SerializerBookInterface
    ) -> str:
        return serialize_instance.serializer_book(book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay.display(
                book,
                ConsoleDisplay() if method_type == "console"
                else ReverseDisplay()
            )
        elif cmd == "print":
            BookPrint.print_book(
                book,
                ConsolePrint() if method_type == "console" else ReversePrint()
            )
        elif cmd == "serialize":
            return BookSerializer.serializer(
                book,
                JsonSerializer() if method_type == "json" else XMLSerializer()
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
