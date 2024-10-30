from app.displayers import BaseDisplay
from app.printers import BasePrint
from app.serializers import BaseSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, method_type: BaseDisplay) -> None:
        method_type.display(self.content)

    def print_book(self, method_type: BasePrint) -> None:
        method_type.print_book(self.title, self.content)

    def serialize(self, method_type: BaseSerializer) -> str:
        return method_type.serialize(self.title, self.content)
