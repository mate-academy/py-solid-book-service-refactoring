from app.utils.handlers import Display, Print, Serialize


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_handler: Display) -> None:
        display_handler.display(self.content)

    def print_book(self, print_handler: Print) -> None:
        print_handler.print(self.title, self.content)

    def serialize(self, serialize_handler: Serialize) -> str:
        return serialize_handler.serialize(self.title, self.content)
