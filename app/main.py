from app.book import Book
from app.command_handler import CommandHandler


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    handler = CommandHandler()
    for cmd, method_type in commands:
        result = handler.execute(book, cmd, method_type)
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
