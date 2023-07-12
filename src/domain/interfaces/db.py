"""db."""
from abc import ABC, abstractmethod


class DbInterface(ABC):
    """DB interface."""

    @abstractmethod
    def create_table():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def validate_table_register():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def validate_user_existence():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def validate_register_existence():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def get_user_id():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def insert_values():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def select():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def delete():
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")
