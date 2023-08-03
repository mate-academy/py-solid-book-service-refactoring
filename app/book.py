import json
import xml.etree.ElementTree as ET # noqa
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

    def check_data_type(self, income_data: str) -> [None, Exception]:
        if income_data not in self.__valid_data:
            raise ValueError(f"Unknown data type: {income_data}")


class BookInitialization:
    def __init__(self, data_type: str) -> None:
        self.data_type = data_type


class DisplayBook(DoAction, BookInitialization, BookValidation):
    def display_book_info(self, book: Book) -> None:
        self.check_data_type(self.data_type)
        if self.data_type == "console":
            print(book.content)
        elif self.data_type == "reverse":
            print(book.content[::-1])


class PrintBook(DoAction, BookInitialization, BookValidation):
    def display_book_info(self, book: Book) -> None:
        self.check_data_type(self.data_type)
        if self.data_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif self.data_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])


class SerializeBook(DoAction, BookInitialization, BookValidation):
    def display_book_info(self, book: Book) -> str:
        self.check_data_type(self.data_type)
        if self.data_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif self.data_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = book.title
            content = ET.SubElement(root, "content")
            content.text = book.content
            return ET.tostring(root, encoding="unicode")
