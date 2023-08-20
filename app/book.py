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
    def console(self, book: Book) -> None:
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(book.content[::-1])


class PrintBook(ViewBook):
    def console(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class ShowContent:
    def __init__(self, view: ViewBook) -> None:
        self.view = view

    def show_content(self, book: Book, method_type: str) -> None:
        if method_type == "console":
            self.view.console(book)
        elif method_type == "reverse":
            self.view.reverse(book)
        else:
            raise ValueError(f"Unknown display type: {method_type}")
