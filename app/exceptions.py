class PublicationException(Exception):
    """Base class for all publication-related exceptions."""
    pass


class DisplayException(PublicationException):
    """Exception raised during display of publication content."""
    def __init__(
        self,
        message: str = "An error occurred during display"
    ) -> None:
        super().__init__(message)


class PrintException(PublicationException):
    """Exception raised during printing of publication content."""
    def __init__(
        self,
        message: str = "An error occurred during printing"
    ) -> None:
        super().__init__(message)


class SerializationException(PublicationException):
    """Exception raised during serialization of publication content."""
    def __init__(
        self,
        message: str = "An error occurred during serialization"
    ) -> None:
        super().__init__(message)
