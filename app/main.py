from app.displayers import DISPLAYERS
from app.printers import PRINTERS
from app.serializers import SERIALIZERS


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = DISPLAYERS.get(method_type)
            if not displayer:
                raise ValueError(f"Unknown display type: {method_type}")
            displayer.display(book.content)

        elif cmd == "print":
            printer = PRINTERS.get(method_type)
            if not printer:
                raise ValueError(f"Unknown print type: {method_type}")
            printer.print_book(book.title, book.content)

        elif cmd == "serialize":
            serializer = SERIALIZERS.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
