from app.models.book import Book
from app.factory.command_factory import command_factory


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None

    for cmd, mode in commands:
        command = command_factory(cmd, mode)
        result = command.execute(book)

    return result


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")

    print(main(
        book,
        [("display", "reverse"), ("serialize", "xml")]
    ))
