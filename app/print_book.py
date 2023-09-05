from app.book import Book


class PrintBook:
    @staticmethod
    def print_book_console(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    @staticmethod
    def print_book_reverse(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content[::-1])

    @classmethod
    def print_book(cls, book: Book, method_type: str) -> None:
        if method_type == "console":
            cls.print_book_console(book)
        elif method_type == "reverse":
            cls.print_book_reverse(book)
        else:
            raise ValueError(f"Unknown print type: {method_type}")

