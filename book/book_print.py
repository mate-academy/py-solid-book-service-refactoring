from book.book import Book


class PrintBook(Book):
    def __init__(self, book: Book) -> None:
        super().__init__(title=book.title, content=book.content)

    def print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}")
        print(self.content[::-1])
