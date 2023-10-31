from app.book import Book
from app.book_processor import BookProcessor


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "serialize":
            return BookProcessor(book, cmd, method_type).run_command()
        BookProcessor(book, cmd, method_type).run_command()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("print", "reverse"),
                ("display", "reverse"),
                ("serialize", "xml")
            ]
        )
    )
