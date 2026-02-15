from app.models import Book


class BookValidator:
    @staticmethod
    def validate(book: Book) -> None:
        if not book.title:
            raise ValueError("Title cannot be empty")
        if not book.content:
            raise ValueError("Content cannot be empty")
