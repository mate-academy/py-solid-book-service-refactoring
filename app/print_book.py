from app.book import Book


class PrintStrategy:
    def print_book(self, book: Book) -> None:
        raise NotImplementedError("Print book is not implemented yet")


class ConsolePrintStrategy(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}")
        print(book.content)


class ReversePrintStrategy(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}")
        print(book.content[::-1])
