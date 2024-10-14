from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, content: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    def display(self, content: str) -> None:
        print(content[::-1])


class DisplayCMD:
    __DISPLAY_TPES = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    @classmethod
    def display(cls, display_type: str, book: object) -> None:
        display_cls = cls.__DISPLAY_TPES.get(display_type)
        if display_cls:
            return display_cls.display(book.content)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
