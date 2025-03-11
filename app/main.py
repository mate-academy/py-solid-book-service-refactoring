from typing import List, Tuple, Optional

from app.handlers import handle_display, handle_serialize, handle_print
from app.book import Book


COMMANDS = {
    "display": handle_display,
    "print": handle_print,
    "serialize": handle_serialize,
}


def main(book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
    for cmd, method_type in commands:
        handler = COMMANDS.get(cmd)
        if handler is None:
            raise ValueError(f"Unknown command: {cmd}")
        result = handler(book, method_type)
        if result is not None:
            return result
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
