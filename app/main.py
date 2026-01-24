from app.book import Book
from app.command_executor import CommandExecutor


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    executor = CommandExecutor(book)

    for command, method_type in commands:
        result = executor.execute(command, method_type)
        if result is not None:
            return result

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("display", "reverse"),
                ("serialize", "xml"),
            ],
        )
    )
