from app.book.factories.displayer_factory import BookDisplayerFactory
from app.book.factories.method_factory_interface import BookMethodFactory
from app.book.factories.printer_factory import BookPrinterFactory
from app.book.factories.serializer_factory import BookSerializerFactory

from app.book.custom_exceptions.action_exception import UnknownActionTypeError

from typing import Type


class BookActionFactory:
    @staticmethod
    def get_action_factory(action_type: str) -> Type[BookMethodFactory]:
        match action_type:
            case "display":
                return BookDisplayerFactory
            case "print":
                return BookPrinterFactory
            case "serialize":
                return BookSerializerFactory
        raise UnknownActionTypeError(action_type)
