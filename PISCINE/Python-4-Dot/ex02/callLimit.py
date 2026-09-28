def callLimit(limit: int):
    """
    Create a decorator that limits how many times a function can be called.

    Note: the counter lives in this outer scope, so it is shared by every
    function decorated with the same `callLimit(...)` instance.

    :param limit: Maximum number of calls allowed before the function is blocked.
    :return: A decorator (callLimiter) to apply to a function.
    """
    count = 0

    def callLimiter(function):
        """
        Decorate a function so it can only be called `limit` times.

        :param function: The function to wrap.
        :return: The wrapper function (limit_function) that enforces the limit.
        """
        def limit_function(*args, **kwargs):
            """
            Call the original function if the limit has not been reached.

            :param args: Positional arguments forwarded to the original function.
            :param kwargs: Keyword arguments forwarded to the original function.
            :return: The original function's result, or None if the limit was reached.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            else:
                count += 1
                return function(*args, **kwargs)

        return limit_function

    return callLimiter
