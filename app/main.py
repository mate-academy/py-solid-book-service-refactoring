from app.book import Book
from app.executor import CommandExecutor


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    executor = CommandExecutor()
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                executor.execute_display(method_type, book)
            elif cmd == "print":
                executor.execute_print(method_type, book)
            elif cmd == "serialize":
                return executor.execute_serialize(method_type, book)
            else:
                raise ValueError(f"Unknown command: {cmd}")
        except ValueError as e:
            raise e


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
