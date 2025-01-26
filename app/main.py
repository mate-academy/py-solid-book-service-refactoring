from app.book import Book
from app.command_handler import Command


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_handler = Command()
    for cmd in commands:
        if result := command_handler.execute(cmd, book):
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
