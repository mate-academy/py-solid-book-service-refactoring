from app.operations import BookOutputOperation


class GetOutputService:
    def __init__(self, operations: dict) -> None:
        self.operations = operations

    def get_operation(self, operation: tuple[str, str]) -> BookOutputOperation:
        service = self.operations.get(operation)
        if service is None:
            raise ValueError(f"Unknown {operation[0]} type: {operation[1]}")

        return service
