from app.book_display import BOOK_DISPLAY_PROCESSORS
from app.book_printer import BOOK_PRINT_PROCESSORS
from app.book_serializer import BOOK_SERIALIZE_PROCESSORS


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        processor = BOOK_DISPLAY_PROCESSORS.get(display_type)

        if processor:
            processor().display(self.content)
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def print_book(self, print_type: str) -> None:
        processor = BOOK_PRINT_PROCESSORS.get(print_type)

        if processor:
            processor().print_book(self.title, self.content)
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def serialize(self, serialize_type: str) -> str:
        processor = BOOK_SERIALIZE_PROCESSORS.get(serialize_type)

        if processor:
            return processor().serialize(self.title, self.content)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
