from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializer = Serializer()

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                strategy = ConsoleDisplay()
            else:
                strategy = ReverseDisplay()
            strategy.display_book(book)
        elif cmd == "print":
            if method_type == "console":
                strategy = ConsolePrint()
            else:
                strategy = ReversePrint()
            strategy.print_book(book)
        elif cmd == "serialize":
            return serializer.serialize(book, method_type)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    book = Book("SOLID Book", "Clean code is beautiful.")
    result = main(book, [("display", "console"), ("serialize", "json")])
    if result:
        print("\nSerialized output:\n", result)
