from typing import TypeVar

from app.book import Book
from app.display import DISPLAY_TYPES
from app.printer import PRINT_TYPES
from app.serializer import SERIALIZE_TYPES

T = TypeVar("T")


def get_handler(handlers: dict[str, T], method_type: str, kind: str) -> T:
    if method_type not in handlers:
        raise ValueError(f"Unknown {kind} type: {method_type}")
    return handlers[method_type]


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            get_handler(DISPLAY_TYPES, method_type, "display").display(book)
        elif cmd == "print":
            get_handler(PRINT_TYPES, method_type, "print").print_book(book)
        elif cmd == "serialize":
            return get_handler(
                SERIALIZE_TYPES, method_type, "serialize"
            ).serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
