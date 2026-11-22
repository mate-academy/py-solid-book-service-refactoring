class UnknownSerializeTypeError(ValueError):
    def __init__(self, serialize_type: str) -> None:
        super().__init__(f"Unknown serialize type: {serialize_type}")
