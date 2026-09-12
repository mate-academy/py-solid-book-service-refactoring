from app.factories import get_displayer, get_printer, get_serializer
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            get_displayer(method_type).display(book)
        elif cmd == "print":
            get_printer(method_type).print_book(book)
        elif cmd == "serialize":
            return get_serializer(method_type).serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")
