from app.book_service.book import Book
from app.book_service.create_processors import (
    create_display_processor,
    create_print_processor,
    create_serialize_processor
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_processor = create_display_processor(method_type)
            display_processor(
                content=book.content
            )
        elif cmd == "print":
            print_processor = create_print_processor(method_type)
            print_processor(
                title=book.title,
                content=book.content
            )
        elif cmd == "serialize":
            serialize_processor = create_serialize_processor(method_type)
            return serialize_processor(
                title=book.title,
                content=book.content
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
