from app.models import Book


class BasePrintStrategy:
    def print(self, book: Book) -> None:
        raise NotImplementedError


class ConsolePrinter(BasePrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(BasePrintStrategy):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookPrinter:
    _strategies = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }

    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        strategy = BookPrinter._strategies.get(print_type)
        if not strategy:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print(book)
