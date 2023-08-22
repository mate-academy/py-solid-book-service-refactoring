from app.book import Book


class Print:
    @staticmethod
    def console_print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    @staticmethod
    def reverse_print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])

    @classmethod
    def print_by_type(cls, print_type: str, book: Book) -> None:
        if print_type == "console":
            cls.console_print(book)
        elif print_type == "reverse":
            cls.reverse_print(book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
