from app.interface import IDisplayStrategy, IPrintStrategy, ISerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, display_strategy: IDisplayStrategy) -> None:
        display_strategy.display(self.content)

    def print_book(self, print_strategy: IPrintStrategy) -> None:
        print_strategy.print_book(self.title, self.content)

    def serialize(self, serializer: ISerializer) -> str:
        return serializer.serialize(self.title, self.content)
