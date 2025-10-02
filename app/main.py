from app.display import get_display_strategy
from app.printer import get_print_strategy
from app.serializer import get_serializer


class Book:
    def __init__(self, title: str, content: str,) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        strategy = get_display_strategy(display_type)
        strategy.display(self.content)

    def print_book(self, print_type: str) -> None:
        strategy = get_print_strategy(print_type)
        strategy.print(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        serializer = get_serializer(serialize_type)
        return serializer.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
