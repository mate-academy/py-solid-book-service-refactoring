from app.commands.base import Command
from app.processors.serialize import SerializeProcessor
from app.models.book import Book


class SerializeCommand(Command):
    def __init__(self, serializer: SerializeProcessor):
        self._serializer = serializer

    def execute(self, book: Book):
        return self._serializer.serialize(book)
