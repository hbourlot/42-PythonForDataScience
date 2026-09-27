

def _get_mean(*args) -> int | float:
    """Calculate the mean of the given values.

    Args:
        *args (int | float): Values used to calculate the mean.

    Returns:
        int | float: The mean of the values.
    """
    total = 0
    for val in args:
        total += val
    return total / len(args)

def _get_median(*args) -> int | float:
    """Calculate the median of the given values.

    Args:
        *args (int | float): Values used to calculate the median.

    Returns:
        int | float: The median of the values.
    """
    values = sorted(args)
    middle = len(values) // 2

    if len(values) % 2 == 0:
        return (values[middle - 1] + values[middle]) / 2
    return values[middle]

def _get_percentile(values, percent) -> int | float:
    """Get the value corresponding to a given percentile.

    Args:
        values (list): Sorted list of values.
        percent (int | float): Percentile to calculate.

    Returns:
        int | float: Value corresponding to the percentile.
    """
    total = len(values)
    index = int((percent * total) // 100)

    return values[index]



def _get_quartile(*args) -> list:
    """Calculate the first and third quartiles.

    Args:
        *args (int | float): Values used to calculate the quartiles.

    Returns:
        list: First and third quartile values.
    """
    sort = sorted(args)
    return [float(_get_percentile(sort ,25)), float(_get_percentile(sort ,75))]

def _get_variance(*args) -> int | float:
    """Calculate the variance of the given values.

    Args:
        *args (int | float): Values used to calculate the variance.

    Returns:
        int | float: The variance of the values.
    """
    mean = _get_mean(*args)

    square_diff = [ (v - mean) ** 2  for v in args]
    total = 0

    for v in square_diff:
        total += v

    avg = total / len(args)

    return avg

def _get_std(*args) -> int | float:
    """Calculate the standard deviation of the given values.

    Args:
        *args (int | float): Values used to calculate the standard deviation.

    Returns:
        int | float: The standard deviation of the values.
    """
    return _get_variance(*args) ** 0.5


def ft_statistics(*args, **kwargs) -> None:
    """Calculate and print requested statistics.

    Args:
        *args (int | float): Values used to calculate the statistics.
        **kwargs (str): Names of the statistics to calculate.

    Returns:
        None: This function only prints the requested statistics.
    """

    for word in ["mean", "median", "quartile", "std", "var"]:
        if len(args) == 0 and word in kwargs.values():
            print("ERROR")
    if len(args) == 0:
        return None

    for word in kwargs.values():
        if word == "mean":
            print("mean : ", _get_mean(*args))
        elif "median" == word:
            print("median : ", _get_median(*args))
        elif "quartile" == word:
            print("quartile : ", _get_quartile(*args))
        elif "std" == word:
            print("std : ", _get_std(*args))
        elif "var" == word:
            print("var : ", _get_variance(*args))


    return None




