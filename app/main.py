from app.display import DisplayService
from app.print_book import PrintBookService
from app.serialize import SerializeService


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookService:
    def __init__(
            self,
            book: Book,
            display_service: DisplayService,
            print_book_service: PrintBookService,
            serialize_service: SerializeService
    ) -> None:
        self.book = book
        self.display_service = display_service
        self.print_book_service = print_book_service
        self.serialize_service = serialize_service

    def display(self, method_type: str) -> None:
        return self.display_service.handle_display(
            method_type,
            self.book.content
        )

    def print_book(self, method_type: str) -> None:
        return self.print_book_service.handle_print_book(
            method_type,
            self.book.title,
            self.book.content
        )

    def serialize(self, method_type: str) -> str:
        return self.serialize_service.handle_serialize(
            method_type,
            self.book.title,
            self.book.content
        )


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_service = DisplayService()
    print_book_service = PrintBookService()
    serialize_service = SerializeService()
    book_service = BookService(
        book,
        display_service,
        print_book_service,
        serialize_service
    )
    for cmd, method_type in commands:
        if cmd == "display":
            book_service.display(method_type)
        elif cmd == "print":
            book_service.print_book(method_type)
        elif cmd == "serialize":
            return book_service.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
