from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King"""

    def __init__(self, name, is_alive=True):
        """Initialize King class

        Args:
            name (str): class name
            is_alive (bool, optional): Whether the character is alive.
                Defaults to True.
        """
        super().__init__(name, is_alive)

    def set_eyes(self, value):
        """Set eyes

        Args:
            value (str): New eyes color
        """
        self.eyes = value

    def get_eyes(self):
        """Getter Eyes"""
        return self.eyes

    def set_hairs(self, value):
        """Set Hairs

        Args:
            value (str): New hairs color
        """
        self.hairs = value

    def get_hairs(self):
        """Get Hairs"""
        return self.hairs
