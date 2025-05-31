from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializer = Serializer()

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = ConsoleDisplay() if method_type == "console" else ReverseDisplay()
            strategy.display_book(book)
        elif cmd == "print":
            strategy = ConsolePrint() if method_type == "console" else ReversePrint()
            strategy.print_book(book)
        elif cmd == "serialize":
            return serializer.serialize(book, method_type)


if __name__ == "__main__":
    book = Book("SOLID Book", "Clean code is beautiful.")
    result = main(book, [("display", "console"), ("serialize", "json")])
    if result:
        print("\nSerialized output:\n", result)
