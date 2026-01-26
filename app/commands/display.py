from app.commands.base import Command
from app.processors.display import DisplayProcessor
from app.models.book import Book


class DisplayCommand(Command):
    def __init__(self, display: DisplayProcessor):
        self._display = display

    def execute(self, book: Book):
        self._display.display(book)
