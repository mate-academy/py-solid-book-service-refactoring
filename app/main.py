from commands import COMMANDS
from models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command_handler = COMMANDS.get(cmd)

        if not command_handler:
            raise ValueError(f"Unknown command: {cmd}")

        result = command_handler.execute(book, method_type)

        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
