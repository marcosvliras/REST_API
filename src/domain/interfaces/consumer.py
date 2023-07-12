"""init."""
from abc import ABC, abstractmethod


class ConsumerInterface(ABC):
    """Api consumer Interface."""

    @abstractmethod
    def get(self):
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")
