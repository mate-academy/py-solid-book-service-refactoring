from app.models import Book
from app.display import get_display
from app.printer import get_printer
from app.serializers import get_serializer


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = get_display(method_type)
            strategy.display(book)

        elif cmd == "print":
            strategy = get_printer(method_type)
            strategy.print(book)

        elif cmd == "serialize":
            serializer = get_serializer(method_type)
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
