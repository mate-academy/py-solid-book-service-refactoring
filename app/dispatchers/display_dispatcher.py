class DisplayDispatcher:
    def __init__(
            self,
            allowed_displayers: dict
    ) -> None:
        self.allowed_displayers = allowed_displayers

    def handle(self, method_type: str) -> None:
        if self.__is_display_type_valid(method_type):
            return self.allowed_displayers[method_type].display()
        raise ValueError(f"Unknown display type: {method_type}")

    def __is_display_type_valid(self, method_type: str) -> bool:
        return method_type in self.allowed_displayers
