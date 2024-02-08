from app.book import Book
from app.commands import COMMANDS


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        result = COMMANDS.get(cmd)[method_type](book)

        if cmd == "serialize":
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
