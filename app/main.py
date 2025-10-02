from app.books import Book
from app.serializers import JsonBookSerializer, XmlBookSerializer

if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")

    sample_book.display()
    sample_book.display()
    sample_book.print_book()
    sample_book.reverse_print_book()
    json_serializer = JsonBookSerializer(sample_book)
    xml_serializer = XmlBookSerializer(sample_book)
    print(json_serializer.serialize(sample_book))
    print(xml_serializer.serialize(sample_book))
