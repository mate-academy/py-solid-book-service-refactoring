from typing import Union, Optional
from app.interface import DisplayInterface, SerializeInterface


ExecutorType = Union[DisplayInterface, SerializeInterface]


class CommandRegistry:
    def __init__(self) -> None:
        self._commands = {}

    def register(
            self,
            cmd_type: str,
            method_type: str, executor: ExecutorType) -> None:
        self._commands[(cmd_type, method_type)] = executor

    def get_executor(
            self,
            cmd_type: str,
            method_type: str
    ) -> Optional[ExecutorType]:
        return self._commands.get((cmd_type, method_type))


registry = CommandRegistry()
