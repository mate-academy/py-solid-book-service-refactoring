from abc import ABC, abstractmethod


class PrintBookInterface(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        raise NotImplementedError


class ConsolePrintBook(PrintBookInterface):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrintBook(PrintBookInterface):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class PrintBookService:
    allowed_print_types = {
        "console": ConsolePrintBook,
        "reverse": ReversePrintBook
    }

    def _is_allowed_print_type_valid(self, print_book_type: str) -> bool:
        return print_book_type in self.allowed_print_types

    def handle_print_book(
            self,
            print_type: str,
            title: str,
            content: str
    ) -> None:
        if self._is_allowed_print_type_valid(print_type):
            self.allowed_print_types[print_type]().print_book(title, content)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
