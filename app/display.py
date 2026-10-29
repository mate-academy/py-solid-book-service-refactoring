from app.action import Action
from app.book import Book


class DisplayConsole(Action):
    def action(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Action):
    def action(self, book: Book) -> None:
        print(book.content[::-1])
