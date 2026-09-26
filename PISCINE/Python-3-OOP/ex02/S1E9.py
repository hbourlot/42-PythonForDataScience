from abc import ABC, abstractmethod


class Character(ABC):
    """Character base class."""

    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Initialize a character.

        Args:
            name (str): Name of a character.
            is_alive (bool, optional): Whether the character is alive.
                Defaults to True.
        """
        self.first_name = name
        self.is_alive = is_alive


class Stark(Character):
    """ "Stark class inheriting from Character."""

    def __init__(self, name, is_alive=True):
        """Initialize a Stark character.

        Args:
            name (str): Name of the character.
            is_alive (bool, optional): Whether the character is alive.
                Defaults to True.
        """
        super().__init__(name, is_alive)

    def die(self):
        """Kill the character."""
        self.is_alive = False
