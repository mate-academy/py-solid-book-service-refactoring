from app.models import Book
from app.registry import get_strategy


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        strategy = get_strategy(command, method_type)

        if command == "display":
            strategy.display(book)
        elif command == "print":
            strategy.print_book(book)
        elif command == "serialize":
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    res = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if res:
        print(res)
