from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class ViewBook(ABC):
    @abstractmethod
    def console(self, book: Book) -> None:
        pass

    @abstractmethod
    def reverse(self, book: Book) -> None:
        pass


class Display(ViewBook):
    def __init__(self, method_type: str) -> None:
        self.method_type = method_type

    def console(self, book: Book) -> None:
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(book.content[::-1])


class PrintBook(ViewBook):
    def __init__(self, method_type: str) -> None:
        self.method_type = method_type

    def console(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
