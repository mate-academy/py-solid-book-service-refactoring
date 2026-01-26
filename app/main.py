from __future__ import annotations
from typing import Optional

from .book import Book
from .executor import BookCommandExecutor, Command


def main(book: Book, commands: list[tuple[str, str]]) -> Optional[str]:
    executor = BookCommandExecutor()
    command_objs = [Command(cmd, method_type) for cmd, method_type in commands]
    return executor.execute(book, command_objs)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
