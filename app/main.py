from app.books import Book
from app.display_service import DisplayService
from app.print_service import PrintService
from app.serialize_service import SerializeService


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayService.display(book.content, method_type)
        elif cmd == "print":
            PrintService.print_book(book.title, book.content, method_type)
        elif cmd == "serialize":
            return SerializeService.serialize(
                book.title,
                book.content,
                method_type
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
