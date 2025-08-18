from app.displays import DisplayInterface
from app.printers import PrinterInterface
from app.serializers import SerializerInterface


class Book:
    def __init__(self, title: str, content: str) -> "Book":
        self.title = title
        self.content = content

    def display(self, display: DisplayInterface) -> None:
        display.display(content=self.content)

    def print_book(self, printer: PrinterInterface) -> None:
        printer.print(content=self.content, title=self.title)

    def serialize(self, serializer: SerializerInterface) -> str:
        return serializer.serialize(title=self.title, content=self.content)
