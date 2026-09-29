import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array and display its original and new shape.

    Args:
        family (list): 2D list representing the family data.
        start (int): Starting index of the slice.
        end (int): Ending index of the slice.

    Returns:
        list: The sliced family data.
    """
    total_len = len(family)
    block_len = len(family[0])

    family_np = 0
    try:
        family_np = np.array(family)[start:end]
        print(f"My shape is : ({total_len}, {block_len})")
        print(f"My new shape is : ({len(family_np)}, {block_len})")
    except AssertionError:
        return []

    return family_np
