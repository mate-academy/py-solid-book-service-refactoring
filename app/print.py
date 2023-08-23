from app.book import Book


class PrintBook:
    def __init__(self, book: Book, print_type: str) -> None:
        self.book = book
        self.print_type = print_type

    def print_book(self) -> None:
        if self.print_type == "console":
            print(f"Printing the book: {self.book.title}...")
            print(self.book.content)
        elif self.print_type == "reverse":
            print(f"Printing the book in reverse: {self.book.title}...")
            print(self.book.content[::-1])
