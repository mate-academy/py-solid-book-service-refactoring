from app.book import Book


class Displayer:
    def display(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleDisplayer(Displayer):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(Displayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
