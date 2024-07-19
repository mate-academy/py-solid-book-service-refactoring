from app.abstract_classes import IBookPrint, IBookSerializer
from app.book_display import ConsoleBookDisplay, ReverseBookDisplay
from app.book_print import ConsoleBookPrint, ReverseBookPrint
from app.serializers import JSONBookSerializer, XMLBookSerializer


class CommandHandler:
    @staticmethod
    def handle_command(cmd, method_type, book):
        result = {}
        if cmd == "display":
            if method_type == "console":
                display_strategy = ConsoleBookDisplay()
            elif method_type == "reverse":
                display_strategy = ReverseBookDisplay()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            result = display_strategy.display(book)
        elif cmd == "print":
            print_strategy: IBookPrint
            if method_type == "console":
                print_strategy = ConsoleBookPrint()
            elif method_type == "reverse":
                print_strategy = ReverseBookPrint()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            result = print_strategy.print(book)
        elif cmd == "serialize":
            serialize_strategy: IBookSerializer
            if method_type == "json":
                serialize_strategy = JSONBookSerializer()
            elif method_type == "xml":
                serialize_strategy = XMLBookSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            result = serialize_strategy.serialize(book)
        return result
