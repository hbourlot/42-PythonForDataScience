class calculator:
    """Calculator class for performing operations on a vector."""

    def __init__(self, vector: list):
        """Initialize a calculator with a vector.

        Args:
            vector (list): List of numeric values to calculate on.
        """
        self._val = vector

    def _calculate(self, operator: str, object) -> None:
        """Apply an arithmetic operation to every value in the vector.

        Args:
            operator (str): Arithmetic operator to apply.
            object: Value used in the arithmetic operation.
        """
        for i in range(0, len(self._val), 1):
            if operator == "+":
                self._val[i] += object
            elif operator == "*":
                self._val[i] *= object
            elif operator == "-":
                self._val[i] -= object
            else:
                if object != 0:
                    self._val[i] /= object

    def __add__(self, object) -> None:
        """Add a value to every element of the vector.

        Args:
            object: Value to add to each element.
        """
        self._calculate("+", object)
        print(self._val)

    def __mul__(self, object) -> None:
        """Multiply every element of the vector by a value.

        Args:
            object: Value to multiply each element by.
        """
        self._calculate("*", object)
        print(self._val)

    def __sub__(self, object) -> None:
        """Subtract a value from every element of the vector.

        Args:
            object: Value to subtract from each element.
        """
        self._calculate("-", object)
        print(self._val)

    def __truediv__(self, object) -> None:
        """Divide every element of the vector by a value.

        Args:
            object: Value to divide each element by.
        """
        self._calculate("/", object)
        print(self._val)
