from app.book import Book


class Display:
    @staticmethod
    def display_console(book: Book) -> None:
        print(book.content)

    @staticmethod
    def display_reverse(book: Book) -> None:
        print(book.content[::-1])

    @classmethod
    def display(cls, book: Book, method_type: str) -> None:
        if method_type == "console":
            cls.display_console(book)
        elif method_type == "reverse":
            cls.display_reverse(book)
        else:
            raise ValueError(f"Unknown display type: {method_type}")
