from app.printing_services import BookContent, BookPrint
from app.serializers import BookSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookContent.method_print(book, method_type)
        elif cmd == "print":
            BookPrint.method_print(book, method_type)
        elif cmd == "serialize":
            return BookSerializer.serializer(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "console"), ("serialize", "xml")]))
