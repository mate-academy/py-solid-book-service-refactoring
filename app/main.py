from app.display import BookDisplay
from app.serialization import BookSerialization


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay.display(book, method_type)
        elif cmd == "print":
            BookDisplay.print_book(book, method_type)
        elif cmd == "serialize":
            return BookSerialization.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    main(sample_book, [("display", "reverse"), ("serialize", "xml")])
