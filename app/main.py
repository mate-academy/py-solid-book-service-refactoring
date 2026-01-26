from typing import Callable

from app.book import Book
from app.displayer import Displayer
from app.printer import Printer
from app.serializer import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str | Callable:
    for cmd, method_type in commands:
        if cmd == "display":
            display = Displayer(book)
            display.display(method_type)
        elif cmd == "print":
            to_print = Printer(book)
            to_print.print_content(method_type)
        elif cmd == "serialize":
            to_serialize = Serializer(book)
            return to_serialize.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "reverse"), ("serialize", "xml")]))
