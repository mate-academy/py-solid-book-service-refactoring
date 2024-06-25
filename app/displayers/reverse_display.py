from app.displayers.display_strategy import DisplayStrategy


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content[::-1])
