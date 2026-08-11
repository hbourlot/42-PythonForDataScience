from typing import Callable

avail_units = [1, 5, 4, 6, 2]
avail_units_chr = ["a", "b", "c"]


def my_filter(unit_num: int) -> bool:
    """
    Check if a unit number is greater than 2.

    Args:
            unit_num: A number to check.

    Returns:
            True if unit_num > 2, False otherwise.
    """
    return unit_num > 2


def my_filter_chr(unit: chr) -> bool:
    """Check if there's 'a' occurance"""
    return unit == "a"


def ft_filter(func: Callable[[int], bool], list: list) -> list:
    """
    Filter elements from a list using a function.

    Args:
            func: A function that returns True or False for each element.
            list: The list to filter.

    Returns:
            A new list containing only elements for which func returns True.
    """
    my_list = []
    for value in list:
        if func(value):
            my_list.append(value)
    return my_list


if __name__ == "__main__":

    y = ft_filter(my_filter, avail_units)
    x = ft_filter(my_filter_chr, avail_units_chr)

    print(y)
    print(x)
