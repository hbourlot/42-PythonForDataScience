import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """
    Generate a random identifier.

    :return: A string of 15 random lowercase ASCII letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    """
    Represent a student with an automatically generated login and id.

    :param name: The student's first name.
    :param surname: The student's last name.

    Attributes set automatically (not accepted by ``__init__``):

    :ivar login: The first letter of the name (capitalized) followed by the
        surname, e.g. ``"Eagle"``.
    :ivar id: A random 15-letter lowercase identifier, unique per instance
        (with very high probability).
    """
    name: str
    surname: str
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Build the login from the name and surname after ``__init__`` runs.

        :return: None
        """
        self.login = self.name[0].capitalize() + self.surname
