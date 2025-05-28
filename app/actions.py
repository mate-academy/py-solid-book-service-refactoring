from abc import ABC, abstractmethod
from typing import Optional, Type, Dict
from app.models import Book
from app.serializers import SerializerRegistry


class IBookAction(ABC):
    @abstractmethod
    def execute(self, book: Book, method_type: str) -> Optional[str]:
        pass


class DisplayAction(IBookAction):
    def execute(self, book: Book, method_type: str) -> Optional[str]:
        if method_type == "console":
            print(book.content)
        elif method_type == "reverse":
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {method_type}")
        return None


class PrintAction(IBookAction):
    def execute(self, book: Book, method_type: str) -> Optional[str]:
        if method_type == "console":
            print(f"Printing the book: {book.title}...")
            print(book.content)
        elif method_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            print(book.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {method_type}")
        return None


class SerializeAction(IBookAction):
    def execute(self, book: Book, method_type: str) -> Optional[str]:
        serializer = SerializerRegistry.get_serializer(method_type)
        return serializer.serialize(book)


class ActionRegistry:
    _actions: Dict[str, Type[IBookAction]] = {}

    @classmethod
    def register(cls, name: str, action_cls: Type[IBookAction]) -> None:
        cls._actions[name] = action_cls

    @classmethod
    def get_action(cls, name: str) -> IBookAction:
        action_cls = cls._actions.get(name)
        if not action_cls:
            raise ValueError(f"Unknown command: {name}")
        return action_cls()


ActionRegistry.register("display", DisplayAction)
ActionRegistry.register("print", PrintAction)
ActionRegistry.register("serialize", SerializeAction)
