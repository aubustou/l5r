class RuleError(Exception):
    """Base class for exceptions in this module."""


class WrongStateError(RuleError):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message


class EndOfGame(Exception):
    """Base class for all end of game exceptions."""


class EndOfFateDeckError(EndOfGame):
    """Exception raised when the fate deck is empty."""


class EndOfDynastyDeckError(EndOfGame):
    """Exception raised when the dynasty deck is empty."""


class MaximumNumberOfTurnsReached(EndOfGame):
    """Exception raised when the maximum number of turns is reached."""
