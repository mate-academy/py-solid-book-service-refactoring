from app.book import Book


class Display:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.book.content)
        elif display_type == "reverse":
            print(self.book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")
