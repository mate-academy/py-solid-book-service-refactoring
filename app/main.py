from app.commands import CommandHandler
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    handler = CommandHandler()

    for cmd, method in commands:
        result = handler.execute(book, cmd, method)
        if result is not None:
            return result
