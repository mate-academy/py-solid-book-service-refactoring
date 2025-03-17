from app.book import (
    Book,
    DisplayBookHandler,
    PrintBookHandler,
    SerializeBookHandler
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayBookHandler.execute(book, method_type)
        elif cmd == "print":
            PrintBookHandler.execute(book, method_type)
        elif cmd == "serialize":
            return SerializeBookHandler.execute(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
