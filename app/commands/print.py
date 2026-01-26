from app.commands.base import Command
from app.processors.print import PrintProcessor
from app.models.book import Book


class PrintCommand(Command):
    def __init__(self, printer: PrintProcessor):
        self._printer = printer

    def execute(self, book: Book):
        self._printer.print_book(book)
