from utils.base import Base


class Display(Base):
    def display_console(self):
        return self.content

    def display_reverse(self):
        return self.content[::-1]

    def print_console(self):
        print(f"Printing the book: {self.title}...")
        return self.display_console()

    def print_reverse(self):
        print(f"Printing the book in reverse: {self.title}...")
        return self.display_reverse()

    def display(self, display_type: str) -> None:
        try:
            print(getattr(self, f"display_{display_type}")())

        except AttributeError:
            raise ValueError(f"Unknown display type: {display_type}")

    def print(self, print_type: str) -> None:
        try:
            print(getattr(self, f"print_{print_type}")())
        except AttributeError:
            raise ValueError(f"Unknown print type: {print_type}")
