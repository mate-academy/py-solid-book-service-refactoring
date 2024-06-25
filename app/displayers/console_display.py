from app.displayers.display_strategy import DisplayStrategy


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, content: str) -> None:
        print(content)
