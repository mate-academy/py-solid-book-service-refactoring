from .models import Book
from .services import (
    BookDisplayService,
    BookPrintService,
    BookSerializationService,
    BookProcessor
)


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    display_service = BookDisplayService()
    print_service = BookPrintService()
    serialization_service = BookSerializationService()

    processor = BookProcessor(display_service, print_service, serialization_service)

    return processor.process_commands(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    print(result)
