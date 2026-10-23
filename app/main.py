from app.models import Book
from app.factory import StrategyFactory


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = StrategyFactory.get_display(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = StrategyFactory.get_print(method_type)
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = StrategyFactory.get_serialize(method_type)
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
