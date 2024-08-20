class ConsolePrint:
    @staticmethod
    def display(title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)

    def __call__(self, *args, **kwargs) -> None:
        self.display(*args, *kwargs)


class ReversePrint:
    @staticmethod
    def display(title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])

    def __call__(self, *args, **kwargs) -> None:
        self.display(*args, *kwargs)
