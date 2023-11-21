from app.book import Book


class BookDisplay:
    def __init__(self, book: Book) -> None:
        self.book = book

    def console(self) -> None:
        print(self.book.content)

    def reverse(self) -> None:
        print(self.book.content[::-1])
