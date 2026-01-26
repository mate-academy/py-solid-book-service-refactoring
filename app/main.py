from typing import Callable

from app.book import Book
from app.displayer import Displayer
from app.printer import Printer
from app.serializer import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str | Callable:
    command_handlers = {
        "display": Displayer,
        "print": Printer,
        "serialize": Serializer
    }

    for cmd, method_type in commands:
        handler_class = command_handlers.get(cmd)
        if not handler_class:
            raise ValueError(f"Unknown command: {cmd}")


        handler = handler_class(book)

        if cmd == "display":
            handler.display(method_type)
        elif cmd == "print":
            handler.print_content(method_type)
        elif cmd == "serialize":
            return handler.serialize(method_type)

if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "reverse"), ("serialize", "xml")]))
