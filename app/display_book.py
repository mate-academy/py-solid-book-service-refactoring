from app.book import Book


class Display:
    @staticmethod
    def console_display(book: Book) -> None:
        print(book.content)

    @staticmethod
    def reverse_display(book: Book) -> None:
        print(book.content[::-1])

    @classmethod
    def display_by_type(cls, display_type: str, book: Book) -> None:
        if display_type == "console":
            cls.console_display(book)
        elif display_type == "reverse":
            cls.reverse_display(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
