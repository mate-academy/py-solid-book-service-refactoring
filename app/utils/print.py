class ConsolePrint:
    @staticmethod
    def print(title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint:
    @staticmethod
    def print(title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
