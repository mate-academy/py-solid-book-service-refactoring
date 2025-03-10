from typing import Dict, Callable


class PrintMixin:
    def __init__(self) -> None:
        self._print_methods: Dict[str, Callable[[], None]] = {
            "console": self._print_console,
            "reverse": self._print_reverse
        }

    def _print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def _print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def print_book(self, print_type: str) -> None:
        method = self._print_methods.get(print_type)
        if method:
            method()
        else:
            raise ValueError(f"Unknown print type: {print_type}")
