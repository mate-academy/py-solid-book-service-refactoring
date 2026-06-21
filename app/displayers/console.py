from app.displayers.base import Displayer
from app.models.book import Book


class ConsoleDisplayer(Displayer):
    def display(self, book: Book) -> None:
        print(book.content)
