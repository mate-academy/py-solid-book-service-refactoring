from app.book import Book
from app.manage import BookCommandsManager
from app.validators import BookValidator, CommandValidator


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    BookValidator.type_check(book)
    CommandValidator.command_check(commands)

    return BookCommandsManager.action(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
