from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print_content(self, title: str, content: str) -> None:
        pass


class ConsolePrint(Print):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(Print):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class UpperCasePrint(Print):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book in upper case: {title}...")
        print(content.upper())


class LowerCasePrint(Print):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book in lower case: {title}...")
        print(content.lower())


class NoSpacesPrint(Print):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book in lower case: {title}...")
        print("".join(char for char in content.split()))


class PrintCMD:
    __PRINT_TYPES = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
        "upper": UpperCasePrint(),
        "lower": LowerCasePrint(),
        "no_space": NoSpacesPrint(),
    }

    @classmethod
    def print_object(cls, print_type: str, book: object) -> None:
        printer = cls.__PRINT_TYPES.get(print_type)
        if printer:
            printer.print_content(book.title, book.content)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
