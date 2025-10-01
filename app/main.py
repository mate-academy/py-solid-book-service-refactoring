from __future__ import annotations

from typing import List, Tuple, Optional
from models.book import Book


def main(book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)
    return None


if __name__ == "__main__":
    sample = Book("Sample Book", "This is some sample content.")
    print(main(sample, [("display", "reverse"), ("serialize", "xml")]))
