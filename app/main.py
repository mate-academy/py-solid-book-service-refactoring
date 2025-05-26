from app.book import Book
from app.command_executor import CommandExecutor


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        command_executor = CommandExecutor(cmd, method_type, book)
        if value := command_executor.run():
            return value

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
