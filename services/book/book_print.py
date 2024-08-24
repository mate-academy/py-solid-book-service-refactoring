from abc import abstractmethod, ABC


class BookPrint(ABC):
    @abstractmethod
    def print_book(self, title, content) -> any:
        pass


class BookPrintConsole(BookPrint):
    def print_book(self, title, content) -> any:
        print(f"Printing the book: {title}...")
        print(content)


class BookPrintReverse(BookPrint):
    def print_book(self, title, content) -> any:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
