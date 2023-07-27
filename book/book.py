class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class BookPrinter:
    def print_book(self, book: Book) -> None:
        pass


class DisplayConsole(BookPrinter):
    def display_book(self, book: Book) -> None:
        print(book.content)


class ReversDisplayConsole(DisplayConsole):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])


class ConsoleBookPrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
