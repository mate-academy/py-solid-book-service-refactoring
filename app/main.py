from app.models import Book
from app.commands import COMMANDS


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for cmd, method_type in commands:
        command = COMMANDS.get(cmd)
        if not command:
            raise ValueError(f"Unknown command: {cmd}")
        serialize = command.command(book, method_type)
        if serialize is not None:
            result = serialize
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
