from app.factories import get_display_strategy, get_print_strategy, get_serialize_strategy
from app.interfaces import BookDisplayInterface, BookPrintInterface, BookSerializeInterface


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, interface: BookDisplayInterface) -> None:
        interface.display(self.content)

    def print_book(self, interface: BookPrintInterface) -> None:
        interface.print_book(self.title, self.content)

    def serialize(self, strategy: BookSerializeInterface) -> str:
        return strategy.serialize(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(get_display_strategy(method_type))
        elif cmd == "print":
            book.print_book(get_print_strategy(method_type))
        elif cmd == "serialize":
            return book.serialize(get_serialize_strategy(method_type))
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
