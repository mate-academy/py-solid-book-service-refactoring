from app.book import Book

from app.service import BookService
from typing import List, Tuple, Optional


def main(book: Book, commands: List[Tuple[str, str]]) -> Optional[str]:
    service = BookService()

    return service.process(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
