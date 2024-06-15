from app.interfaces import Display, PrintBook, Serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, action: Display) -> None:
        action.display(self.content)

    def print_book(self, action: PrintBook) -> None:
        action.print_book(self.title, self.content)

    def serialize(self, action: Serializer) -> str:
        return action.serialize(self.title, self.content)
