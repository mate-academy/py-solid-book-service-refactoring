from app.models import Book
from app.services import display_book, print_book, serialize_book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        if command == "display":
            display_book(book, method_type)
        elif command == "print":
            print_book(book, method_type)
        elif command == "serialize":
            return serialize_book(book, method_type)

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
