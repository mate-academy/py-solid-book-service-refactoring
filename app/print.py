class PrintBook:
    def print(self, title: str, content: str) -> str:
        raise ValueError("Unknown print type")


class ConsolePrint(PrintBook):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(PrintBook):
    def print(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
