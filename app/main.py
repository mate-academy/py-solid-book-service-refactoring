from app.book_model import Book
from app.command_handler import CommandHandler


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    for cmd, method_type in commands:
        result = CommandHandler().handle_command(
            cmd=cmd,
            method_type=method_type,
            book=book
        )
        return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
