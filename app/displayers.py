from app.models import Book


class ConsoleDisplayer:
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer:
    def display(self, book: Book) -> None:
        print(book.content[::-1])
