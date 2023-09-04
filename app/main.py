from app.book import Book
from app.commands import DISPLAY_COMMANDS, PRINT_COMMANDS, SERIALIZE_COMMANDS


def main(
        book: Book,
        commands: list[tuple[str, str]]
) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            # book.display(method_type)
            DISPLAY_COMMANDS[method_type]().display(book)
        elif cmd == "print":
            # book.print_book(method_type)
            PRINT_COMMANDS[method_type]().print(book)
        elif cmd == "serialize":
            return SERIALIZE_COMMANDS[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
