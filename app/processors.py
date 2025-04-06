from app.display import ConsoleDisplay, ReverseDisplay
from app.printing import ConsolePrint, ReversePrint
from app.serialization import JSONSerializer, XMLSerializer


display_processors = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay()
}
print_processors = {
    "console": ConsolePrint(),
    "reverse": ReversePrint()
}
serializers = {
    "json": JSONSerializer(),
    "xml": XMLSerializer()
}
