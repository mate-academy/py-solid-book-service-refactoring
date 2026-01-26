from typing import List, Tuple, Optional

from .book import Book
from .handlers import DISPLAY_HANDLERS, PRINT_HANDLERS, SERIALIZERS


def main(
    book: Book,
    commands: List[Tuple[str, str]],
) -> Optional[str]:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_HANDLERS[method_type].display(book)
        elif cmd == "print":
            PRINT_HANDLERS[method_type].print(book)
        elif cmd == "serialize":
            return SERIALIZERS[method_type].serialize(book)
