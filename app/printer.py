from app.book import Book


class Printer:
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.book.title}...")
            print(self.book.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.book.title}...")
            print(self.book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")
