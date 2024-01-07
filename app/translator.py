from abc import ABC, abstractmethod

from app.command import DisplayCommand, SerializeCommand, PrintCommand
from app.displayer import ConsoleDisplayer, ReverseDisplayer
from app.serializer import JsonSerializer, XmlSerializer


class Translator(ABC):
    @staticmethod
    @abstractmethod
    def translate(key: str) -> callable:
        ...


class CommandTranslator(Translator):
    @staticmethod
    def translate(key: str) -> callable:
        command_map = {
            "display": DisplayCommand.command,
            "print": PrintCommand.command,
            "serialize": SerializeCommand.command
        }
        try:
            return command_map[key]
        except KeyError:
            raise ValueError(f"Unknown command type: {key}")


class DisplayerTranslator(Translator):
    @staticmethod
    def translate(key: str) -> callable:
        displayer_map = {
            "console": ConsoleDisplayer.display,
            "reverse": ReverseDisplayer.display,
            "json": JsonSerializer.serialize,
            "xml": XmlSerializer.serialize
        }

        try:
            return displayer_map[key]
        except KeyError:
            raise ValueError(f"Unknown displayer type: {key}")
