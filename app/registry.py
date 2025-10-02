from app.displayers import ConsoleBookDisplayer, ReverseBookDisplayer
from app.printers import ConsoleBookPrinter, ReverseBookPrinter
from app.serializers import JsonBookSerializer, XmlBookSerializer

PRINTERS = {
    "console": ConsoleBookPrinter(),
    "reverse": ReverseBookPrinter(),
}
DISPLAYERS = {
    "console": ConsoleBookDisplayer(),
    "reverse": ReverseBookDisplayer(),
}
SERIALIZERS = {
    "json": JsonBookSerializer(),
    "xml": XmlBookSerializer(),
}
