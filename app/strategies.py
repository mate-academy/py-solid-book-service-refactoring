from app.book import Book


class PrintStrategy:
    def print(self, book: Book) -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(book.content)


class ReversePrint(PrintStrategy):
    def print(self, book: Book) -> None:
        print(book.content[::-1])
