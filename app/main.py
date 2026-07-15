from app.book import Book
from app.command_handler import CommandHandler

handler = CommandHandler()


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        result = handler.handle(book, cmd, method_type)
        if result is not None:
            return result
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
