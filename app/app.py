from __future__ import annotations
from typing import List, Tuple, Optional
from book import Book


def main(book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
    """
    Поведінка збережена:
      - "display"  -> виклик Book.display
      - "print"    -> виклик Book.print_book
      - "serialize"-> повертає str і завершуються обхід команд
    """
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
