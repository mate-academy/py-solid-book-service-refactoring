class DisplayStrategy:
    def show(self, content: str) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])


class DisplayStrategyFactory:
    @staticmethod
    def get_strategy(display_type: str) -> DisplayStrategy:
        if display_type == "console":
            return ConsoleDisplay()
        if display_type == "reverse":
            return ReverseDisplay()
        raise ValueError(f"Unknown display type: {display_type}")
