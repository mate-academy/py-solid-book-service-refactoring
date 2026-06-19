from app.book import Book
from app.display import DisplayManager
from app.serializers import SerializationManager


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            try:
                strategy = DisplayManager.get_strategy(method_type)
                strategy.display(book)
            except ValueError:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            try:
                strategy = DisplayManager.get_strategy(method_type)
                strategy.print_book(book)
            except ValueError:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            return SerializationManager.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    print(result)
