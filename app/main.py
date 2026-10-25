"""Main entry point for the book service application.

Following DIP: depends on abstractions (BookService) rather than
concrete implementations. The composition root wires up all
dependencies here.
"""

from app.domain.book import Book
from app.services import BookService


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    """Execute book commands using the BookService.

    Args:
        book: The book to operate on
        commands: List of (command, type) tuples

    Returns:
        The result of the last serialize command, or None
    """
    service = BookService()
    return service.execute_commands(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result:
        print(result)
