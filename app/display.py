from app.book import Book


class DisplayStrategy:
    def display(self, book: Book) -> None:
        raise NotImplementedError("Display method is not implemented yet")


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
