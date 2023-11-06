from app.book.book_service import BookService
from app.book.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> str:
    for cmd, method_type in commands:
        book_service = BookService.create_book_service(book, cmd, method_type)
        return book_service.operate()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
