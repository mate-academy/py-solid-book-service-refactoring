from abc import ABC


class Product(ABC):
    pass


class Book(Product):
    def __init__(self, title: str, content: str) -> None:
        super().__init__()
        self.title = title
        self.content = content
