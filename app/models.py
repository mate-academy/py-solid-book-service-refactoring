from app.displayers import Displayer
from app.printers import Printer
from app.serializers import Serializer


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, displayer: Displayer) -> None:
        return displayer.display(self.content)

    def print_book(self, printer: Printer) -> None:
        return printer.print_book(self.title, self.content)

    def serialize(self, serializer: Serializer):
        return serializer.serialize(self.title, self.content)
