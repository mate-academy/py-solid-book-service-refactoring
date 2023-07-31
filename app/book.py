from app.book_display import BOOK_DISPLAY_PROCESSORS
from app.book_printer import BOOK_PRINT_PROCESSORS
from app.book_serializer import BOOK_SERIALIZE_PROCESSORS


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    @staticmethod
    def _get_processor(processors: dict, method_name: str) -> object:
        if method_name in processors:
            return processors[method_name]()
        raise ValueError(f"Unknown method: {method_name}")

    def display(self, display_type: str) -> None:
        self._get_processor(BOOK_DISPLAY_PROCESSORS, display_type).display(
            self.content
        )

    def print_book(self, print_type: str) -> None:
        self._get_processor(BOOK_PRINT_PROCESSORS, print_type).print_book(
            self.title, self.content
        )

    def serialize(self, serialize_type: str) -> str:
        return self._get_processor(
            BOOK_SERIALIZE_PROCESSORS, serialize_type
        ).serialize(self.title, self.content)
