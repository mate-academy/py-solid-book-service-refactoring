from app.book import Book
from app.print import print_handlers
from app.display import display_handlers
from app.serialize import serialize_handlers

book_handlers = {
    "print": print_handlers,
    "display": display_handlers,
    "serialize": serialize_handlers
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method in commands:
        try:
            action = book_handlers.get(command).get(method)
        except AttributeError:
            raise ValueError(f"Unsupported command: '{command}', with method: '{method}'")

        if command == "serialize":
            return action.exec(book)
        action.exec(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
