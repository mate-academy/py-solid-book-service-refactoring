from app.book import Book
from app.display import display_command
from app.print import print_command
from app.serialize import serialize_command


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_command(book, method_type)

        elif cmd == "print":
            print_command(book, method_type)

        elif cmd == "serialize":
            return serialize_command(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
