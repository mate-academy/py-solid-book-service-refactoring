from app.book import Book
from app.managers import BookManager


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_manager = BookManager(book)
    for cmd, method_type in commands:
        if cmd == "display":
            book_manager.display(method_type)
        elif cmd == "print":
            book_manager.print_book(method_type)
        elif cmd == "serialize":
            return book_manager.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
