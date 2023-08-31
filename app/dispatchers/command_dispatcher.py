class CommandDispatcher:
    RETURN_COMMANDS = ["serialize"]

    def __init__(
            self,
            allowed_dispatcher: dict
    ) -> None:
        self.allowed_dispatcher = allowed_dispatcher

    def handle_output(
            self,
            cmd: str,
            method_type: str,
    ) -> str:
        return self.allowed_dispatcher[cmd].handle(
            method_type=method_type,
        )

    def is_command_valid(self, cmd: str) -> bool:
        return cmd in self.allowed_dispatcher
