from abc import ABC, abstractmethod
from typing import Type

from app.display import ConsoleDisplay, ReverseDisplay, Display
from app.print import ConsolePrint, ReversePrint, Print
from app.serializer import JSONSerializer, XMLSerializer, Serializer


class CommandFabric(ABC):
    @abstractmethod
    def create_command_class(
            self,
            command: str,
    ) -> Type["CommandFabric"]:
        """
        Returns class instance with given command
        Args:
            command: str

        Returns: class object

        """
        pass


class DisplayCommands(CommandFabric):
    def __init__(self) -> None:
        self.commands = {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay()
        }

    def create_command_class(self, command: str) -> Display:
        if command in self.commands:
            return self.commands[command]
        raise ValueError(f"Unknown display type: {command}")


class PrintCommands(CommandFabric):
    def __init__(self) -> None:
        self.commands = {
            "console": ConsolePrint(),
            "reverse": ReversePrint()
        }

    def create_command_class(self, command: str) -> Print:
        if command in self.commands:
            return self.commands[command]
        raise ValueError(f"Unknown print type: {command}")


class SerializerCommands(CommandFabric):
    def __init__(self) -> None:
        self.commands = {
            "json": JSONSerializer(),
            "xml": XMLSerializer()
        }

    def create_command_class(self, command: str) -> Serializer:
        if command in self.commands:
            return self.commands[command]
        raise ValueError(f"Unknown serialize type: {command}")
