class UnknownDisplayTypeError(ValueError):
    def __init__(self, display_type: str) -> None:
        super().__init__(f"Unknown display type: {display_type}")
