from app.display import get_display
from app.print_service import get_book_print_type
from app.serializer import get_serialize_type
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_type = get_display(method_type)
            display_type.display(book)
        elif cmd == "print":
            book_print_type = get_book_print_type(method_type)
            book_print_type.print_book(book)
        elif cmd == "serialize":
            serialize_type = get_serialize_type(method_type)
            return serialize_type.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
