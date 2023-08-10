from app.book import Book
from app.book_display import BOOK_DISPLAY_PROCESSORS
from app.book_printer import BOOK_PRINT_PROCESSORS
from app.book_serializer import BOOK_SERIALIZE_PROCESSORS


BOOK_PROCESSORS = {
    "display": BOOK_DISPLAY_PROCESSORS,
    "print": BOOK_PRINT_PROCESSORS,
    "serialize": BOOK_SERIALIZE_PROCESSORS,

}


def handle_book(book: Book, command: str, method: str) -> None:
    if command in BOOK_PROCESSORS:
        if method in BOOK_PROCESSORS[command]:
            handler = getattr(
                BOOK_PROCESSORS[command][method](), command
            )
            return handler(book.title, book.content)
        raise ValueError(f"Unknown method: {method}")
    raise ValueError(f"Unknown command: {command}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method in commands:
        return handle_book(book, command, method)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
