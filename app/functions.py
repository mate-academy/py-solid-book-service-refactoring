import json
import xml.etree.ElementTree as ElT
from app.classes import Book


def display(display_type: str, book: Book) -> None:
    if display_type == "console":
        print(book.content)
    elif display_type == "reverse":
        print(book.content[::-1])
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def print_book(print_type: str, book: Book) -> None:
    if print_type == "console":
        print(f"Printing the book: {book.title}...")
        print(book.content)
    elif print_type == "reverse":
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def serialize(serialize_type: str, book: Book) -> str:
    if serialize_type == "json":
        return json.dumps({"title": book.title, "content": book.content})
    elif serialize_type == "xml":
        root = ElT.Element("book")
        title = ElT.SubElement(root, "title")
        title.text = book.title
        content = ElT.SubElement(root, "content")
        content.text = book.content
        return ElT.tostring(root, encoding="unicode")
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
