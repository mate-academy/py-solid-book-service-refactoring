from abc import abstractmethod, ABC


class BookPrint(ABC):
    def __init__(self, book: any) -> None:
        self.book = book

    @abstractmethod
    def print_book(self) -> any:
        pass


class BookPrintConsole(BookPrint):
    def print_book(self) -> any:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class BookPrintReverse(BookPrint):
    def print_book(self) -> any:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
