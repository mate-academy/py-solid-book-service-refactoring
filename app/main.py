from dataclasses import dataclass

from app.services.book_service import BookService


@dataclass(frozen=True)
class Book:
    title: str
    content: str


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService()
    return service.execute(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
