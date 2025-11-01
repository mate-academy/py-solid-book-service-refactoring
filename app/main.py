from app.displays import BookDisplay
from app.printer import BookPrinter
from app.serializers import BookSerializer
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    handlers = {
        "display": BookDisplay.display,
        "print": BookPrinter.print_book,
        "serialize": BookSerializer.serialize,
    }

    for cmd, method_type in commands:
        handler = handlers.get(cmd)
        if not handler:
            raise ValueError(f"Unknown command: {cmd}")
        result = handler(book, method_type)
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
