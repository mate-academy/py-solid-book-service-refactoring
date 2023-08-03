import json
import xml.etree.ElementTree as ET  # noqa
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DoAction(ABC):
    @abstractmethod
    def display_book_info(self, book: Book) -> None:
        pass


class Validation(ABC):
    @abstractmethod
    def check_data_type(self, income_data: str) -> None:
        pass


class BookValidation(Validation):
    __valid_data = ["console", "reverse", "json", "xml"]

    def check_data_type(self, income_data: str) -> None:
        if income_data not in self.__valid_data:
            raise ValueError(f"Unknown data type: {income_data}")


class ActionWithBookValidation(DoAction, BookValidation):
    def __init__(self, method_type: str) -> None:
        self.method_type = method_type
        self.check_data_type(method_type)


class ConsoleDisplayBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> None:
        if self.method_type == "console":
            ConsoleDisplayBook(self.method_type).display_book_info(book)
        elif self.method_type == "reverse":
            ReverseDisplayBook(self.method_type).display_book_info(book)


class ConsolePrintBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> None:
        if self.method_type == "console":
            ConsolePrintBook(self.method_type).display_book_info(book)
        elif self.method_type == "reverse":
            ReversePrintBook(self.method_type).display_book_info(book)


class SerializeJsonBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXmlBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class SerializeBook(ActionWithBookValidation):
    def display_book_info(self, book: Book) -> None | str:
        if self.method_type == "json":
            return SerializeJsonBook(self.method_type).display_book_info(book)
        elif self.method_type == "xml":
            return SerializeXmlBook(self.method_type).display_book_info(book)
