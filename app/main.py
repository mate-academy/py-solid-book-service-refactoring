from app.depencies import tuple_to_commands
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    commands = tuple_to_commands(commands)

    for cmd in commands:
        result = cmd.execute(book)

        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
