from app.book import Book


class Displayer:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display_console(self) -> None:
        print(self.book.content)

    def display_reverse(self) -> None:
        print(self.book.content[::-1])

    def display(self, method_type: str) -> None:
        method_name = f"display_{method_type}"
        method = getattr(self, method_name, None)

        if not callable(method):
            raise ValueError(f"Unknown display method: {method_type}")

        method()
