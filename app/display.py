from app.book import Book


class DisplayBook:
    def __init__(self, book: Book, display_type: str) -> None:
        self.book = book
        self.display_type = display_type

    def display(self) -> None:
        if self.display_type == "console":
            print(self.book.content)
        elif self.display_type == "reverse":
            print(self.book.content[::-1])
