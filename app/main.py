from app.books_manager.books import Book
from app.books_manager.command_manager import CommandManager


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        manager = CommandManager(cmd, method_type)

        if manager.performer:
            obj = manager.get_method()(book)
            if obj:
                return obj
        else:
            raise manager.get_error()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
