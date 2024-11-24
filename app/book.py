from app.display import DisplayMethod
from app.print import PrintMethod
from app.serialization import SerializationMethod


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, method: DisplayMethod) -> None:
        method.display(self.content)

    def print_book(self, method: PrintMethod) -> None:
        method.print(self.title, self.content)

    def serialize(self, method: SerializationMethod) -> str:
        return method.serialize(self.title, self.content)
