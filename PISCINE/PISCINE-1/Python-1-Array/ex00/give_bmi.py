def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """Calculate the BMI for each height and weight pair.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List containing the calculated BMI values.
    """

    result = []

    len_h = len(height)
    len_w = len(weight)

    if len_h != len_w:
        return result

    try:
        for i in range(len_h):
            if i >= len(weight):
                break
            result.append(weight[i] / (height[i] ** 2))
    except (TypeError, ZeroDivisionError):
        return []

    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check whether each BMI value is above the given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): BMI threshold to compare against.

    Returns:
        list[bool]: List indicating whether each BMI is above the limit.
    """
    result = []

    try:
        for item in bmi:
            result.append(item > limit)
    except TypeError:
        return []

    return result
