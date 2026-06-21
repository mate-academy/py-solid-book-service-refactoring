from app.displayers.base import Displayer
from app.models.book import Book


class ReverseDisplayer(Displayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
