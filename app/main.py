from app.models import Book
from app.functionality.display_functionality import display_book_func
from app.functionality.print_functionality import print_book_func
from app.functionality.serialize_functionality import serialize_book_func


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book_func(method_type, book.content)
        elif cmd == "print":
            print_book_func(method_type, book.title, book.content)
        elif cmd == "serialize":
            return serialize_book_func(method_type, book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
