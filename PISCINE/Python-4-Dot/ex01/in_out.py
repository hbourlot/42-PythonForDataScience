def square(x: int | float) -> int | float:
    """
    Calculates the square of a number (x to the power of 2).

    :param x: The integer or float number to be squared.
    :return: The result of the number multiplied by itself.
    """
    return x ** 2

def pow(x: int | float) -> int | float:
    """
    Calculates the self-power of a number (x to the power of x).

    :param x: The integer or float number used as both base and exponent.
    :return: The result of the number raised to itself.
    """
    return x ** x

def outer(x: int | float, function) -> object:
    """
    Creates a closure that accumulates the results of successive function calls.

    :param x: The initial numeric value for the first calculation.
    :param function: The mathematical function (e.g., square or pow) to apply.
    :return: The inner function that maintains state inside its persistent memory.
    """
    count = 0
    def inner() -> float:
        """
        Updates the outer 'count' variable by applying the function to the current state.

        :return: The accumulated result of the mathematical operations as a float.
        """
        nonlocal count
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
