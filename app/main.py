from app.book import Book
from app.book_print import PrintBook
from app.book_serializer import SerializerFormat


def run_display(book: Book, method_type: str) -> None:
    book.display(method_type)


def run_print(book: Book, method_type: str) -> None:
    PrintBook(book).print(method_type)


def run_serialize(book: Book, method_type: str) -> str:
    serializer = SerializerFormat.create_serializer(method_type, book)
    return serializer.serialize()


actions = {
    "display": run_display,
    "print": run_print,
    "serialize": run_serialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        return actions[cmd](book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
