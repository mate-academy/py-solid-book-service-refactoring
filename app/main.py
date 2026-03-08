from app.book import Book
from app.strategies.display import display_strategies
from app.strategies.print import print_strategies
from app.strategies.serialize import serializers


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            strategy.print_book(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
