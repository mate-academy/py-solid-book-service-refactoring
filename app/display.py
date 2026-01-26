from .book import Book


class ConsoleDisplay:
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay:
    def display(self, book: Book) -> None:
        print(book.content[::-1])
