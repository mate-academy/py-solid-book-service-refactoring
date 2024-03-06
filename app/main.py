from app.display import display_handlers
from app.print import print_handlers
from app.serializer import serializer_handlers, SerializeFile
from app.book import Book

book_handler = {
    "display": display_handlers,
    "print": print_handlers,
    "serialize": serializer_handlers,
}


def main(book: "Book", commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        handler = book_handler[cmd][method_type]

        if issubclass(handler, SerializeFile):
            return handler().serialize(book)
        handler().display(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
