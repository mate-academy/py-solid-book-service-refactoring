from app.book import Book
from app.display import Display
from app.printer import Printer
from app.serializer import Serializer


def main(book: Book, operations: list[tuple[str, str]]) -> str:
    serialized_data = ""
    for operation, operation_type in operations:
        if operation == "display":
            displayer = Display(book)
            displayer.display(operation_type)
        elif operation == "print":
            printer = Printer(book)
            printer.print_book(operation_type)
        elif operation == "serialize":
            serializer = Serializer(book)
            serialized_data += serializer.serialize(operation_type)
    return serialized_data


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    operations = [
        ("display", "reverse"),
        ("serialize", "json"),
        ("serialize", "xml"),
    ]
    serialized_books = main(sample_book, operations)
