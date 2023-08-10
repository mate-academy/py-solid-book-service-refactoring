from app.book_display import BOOK_DISPLAY_PROCESSORS
from app.book_printer import BOOK_PRINT_PROCESSORS
from app.book_serializer import BOOK_SERIALIZE_PROCESSORS


class Book:
    BOOK_PROCESSORS = {
        "display": BOOK_DISPLAY_PROCESSORS,
        "print": BOOK_PRINT_PROCESSORS,
        "serialize": BOOK_SERIALIZE_PROCESSORS,
    }

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def handle(self, command: str, method: str) -> None:
        if command in self.BOOK_PROCESSORS:
            if method in self.BOOK_PROCESSORS[command]:
                handler = getattr(
                    self.BOOK_PROCESSORS[command][method](), command
                )
                return handler(self.title, self.content)
            raise ValueError(f"Unknown method: {method}")
        raise ValueError(f"Unknown command: {command}")
