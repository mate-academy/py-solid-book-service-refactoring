from app.interfaces import DisplayStrategy


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class DisplayFactory:
    @staticmethod
    def get_display_strategy(display_type: str) -> DisplayStrategy:
        if display_type == "console":
            return ConsoleDisplay()
        elif display_type == "reverse":
            return ReverseDisplay()
        else:
            raise ValueError(f"Unknown display type: {display_type}")
