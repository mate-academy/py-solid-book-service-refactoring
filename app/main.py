from app.book import Book
from app.commands import DisplayCommand, SerializeCommand, PrintCommand


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayCommand(method_type, book).execute()
        if cmd == "print":
            PrintCommand(method_type, book).execute()
        if cmd == "serialize":
            return SerializeCommand(method_type, book).execute()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
