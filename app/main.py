from app.book import Book
from app.managers import BookCommandManager
from app.validators import BookTypeValidator, CommandsValidator


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    BookTypeValidator.type_checker(book=book)
    CommandsValidator.commands_checker(commands=commands)

    return BookCommandManager.perform_actions(book=book, commands=commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
