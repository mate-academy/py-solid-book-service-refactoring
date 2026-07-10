from typing import Iterable

from app.book import Book
from app.factories import DISPLAY_HANDLERS, SERIALIZERS, PRINTERS


def main(book: Book, commands: Iterable) -> None | str:
    for command, mode in commands:
        if command == "display":
            DISPLAY_HANDLERS[mode].display(book.content)

        elif command == "print":
            PRINTERS[mode].print(book)

        elif command == "serialize":
            return SERIALIZERS[mode].serialize(book)
