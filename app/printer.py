class PrinterStrategy:
    def print_book(self, book) -> None:
        raise NotImplementedError


class ConsolePrinter(PrinterStrategy):
    def print_book(self, book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrinterStrategy):
    def print_book(self, book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
