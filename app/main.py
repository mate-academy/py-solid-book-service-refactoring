from app.models.book import Book
from app.services.printer import BookService
from app.services.serializer import BookSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService(book)
    serializer = BookSerialize(book)

    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            service.print_book(method_type)
        elif cmd == "serialize":
            return serializer.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
