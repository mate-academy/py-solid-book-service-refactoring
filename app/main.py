from typing import List, Tuple
from app.book import Book
from app.command import SerializeCommand, DisplayCommand, PrintCommand


def main(book: Book, commands: List[Tuple[str, str]]) -> None | str:
    command_mapping = {
        "display": DisplayCommand,
        "print": PrintCommand,
        "serialize": SerializeCommand,
    }

    result = None

    for cmd, method_type in commands:
        if cmd in command_mapping:
            command_class = command_mapping[cmd]
            command = command_class(method_type)
            result = command.execute(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Пример книги", "Это некоторое примерное содержимое.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
