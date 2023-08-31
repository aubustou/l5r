class RuleError(Exception):
    """Base class for exceptions in this module."""


class WrongStateError(RuleError):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message
