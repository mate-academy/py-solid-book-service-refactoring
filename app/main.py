from app.book import Book
from app.display_manager_ import display_manager
from app.print_manager import print_manager
from app.serialize_manager_ import serialize_manager

actions = {"print": print_manager,
           "display": display_manager,
           "serialize": serialize_manager}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd in actions:
            action = actions.get(cmd)
            return action(method=method_type, book=book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
