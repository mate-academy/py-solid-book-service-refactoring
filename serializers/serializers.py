from book.book import Book


class BookSerializer:
    def serialize(self, book: Book) -> str:
        pass


class JSONBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        import json
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        import xml.etree.ElementTree as Etree
        root = Etree.Element("book")
        title = Etree.SubElement(root, "title")
        title.text = book.title
        content = Etree.SubElement(root, "content")
        content.text = book.content
        return Etree.tostring(root, encoding="unicode")
