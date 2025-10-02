class DisplayStrategy:
    def display(self, content: str) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


def get_display_strategy(display_type: str) -> DisplayStrategy:
    if display_type == "console":
        return ConsoleDisplay()
    if display_type == "reverse":
        return ReverseDisplay()
    raise ValueError(f"Unknown display type: {display_type}")
