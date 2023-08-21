from __future__ import annotations

from app.entities.book import Book
from app.dispatchers.command_dispatcher import CommandDispatcher


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if CommandDispatcher.is_command_valid(cmd):
            output = CommandDispatcher.handle_output(cmd, method_type, book)

            if cmd in CommandDispatcher.RETURN_COMMANDS:
                return output


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
