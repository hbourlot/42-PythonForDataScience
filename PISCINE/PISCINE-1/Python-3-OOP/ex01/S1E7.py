from S1E9 import Character


class Baratheon(Character):
    """Baratheon family class"""

    def __init__(self, name, is_alive=True):
        """Initialize Baratheon family class

        Args:
            name (str): name of class
            is_alive (bool, optional): Whether the character is alive.
                            Defaults to True.
        """
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        return f"Vector :('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return self.__repr__()

    def die(self):
        """Kill the character."""
        self.is_alive = False


class Lannister(Character):
    """Lannister family class"""

    def __init__(self, name, is_alive=True):
        """Initialize family class

        Args:
            name (str): name of class
            is_alive (bool, optional): Whether the character is alive.
                            Defaults to True.
        """
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        return f"Vector :('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return self.__repr__()

    def die(self):
        """Kill the character."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name, is_alive=True):
        return cls(name, is_alive)
