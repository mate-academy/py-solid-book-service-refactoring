from app.book import Book


class Print:
    cmd_type = "print"

    @staticmethod
    def console(book: Book) -> None:
        print(
            f"Printing the book: {book.title}...\n{book.content}"
        )

    @staticmethod
    def reverse(book: Book) -> None:
        print(
            f"Printing the book in reverse: {book.title}...\n"
            f"{book.content[::-1]}"
        )
