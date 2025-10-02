from app.models import Book
from app.service import BookService


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book)
    result = None
    for cmd, method_type in commands:
        result = service.execute(cmd, method_type)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
