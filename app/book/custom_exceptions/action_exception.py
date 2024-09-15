class UnknownActionTypeError(ValueError):
    def __init__(self, action_type: str) -> None:
        super().__init__(f"Unknown action type: {action_type}")
