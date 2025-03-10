from typing import Optional

from app.display_service import ExtendedDisplayMixin, DisplayMixin
from app.models import BookBase
from app.print_service import PrintMixin
from app.serializer__service import SerializeMixin


class Book(
    BookBase, ExtendedDisplayMixin, PrintMixin, SerializeMixin
):
    def __init__(self, title: str, content: str) -> None:
        BookBase.__init__(self, title, content)
        DisplayMixin.__init__(self)
        PrintMixin.__init__(self)
        SerializeMixin.__init__(self)


def main(book: Book, commands: list[tuple[str, str]]) -> Optional[str]:
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            result = book.serialize(method_type)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
