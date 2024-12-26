from abc import ABC, abstractmethod

from app.objects import Book


class OutputObject(ABC):

    @abstractmethod
    def output_object(self) -> None:
        pass

    @abstractmethod
    def output_object_reverse(self) -> None:
        pass


class DisplayBook(OutputObject):

    def output_object(self, book: Book) -> None:
        print(book.content)

    def output_object_reverse(self, book: Book) -> None:
        print(book.content[::-1])


class PrintBook(OutputObject):

    def output_object(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def output_object_reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
