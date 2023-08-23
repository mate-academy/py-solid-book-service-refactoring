from app.book import Book
from app.managers import BookManager


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_manager = BookManager(book, commands)
    return book_manager.performer_actions()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
