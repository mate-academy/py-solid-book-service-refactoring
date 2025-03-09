from app.book.book_model import Book
from app.book.book_service import BookService


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_service = BookService(book)
    return book_service.process_commands(commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
