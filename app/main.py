from app.books import Book
from app.display import get_display_strategy
from app.print import get_print_strategy
from app.serialize import get_serialize_strategy


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = get_display_strategy(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = get_print_strategy(method_type)
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = get_serialize_strategy(method_type)
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
