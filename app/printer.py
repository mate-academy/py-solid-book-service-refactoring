from app.book import Book


class Printer:
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_console(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])

    def print_content(self, method_type: str) -> None:
        method_name = f"print_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown print type: {method_type}")

        method()
