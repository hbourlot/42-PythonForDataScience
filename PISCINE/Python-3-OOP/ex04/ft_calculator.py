class calculator:
    """Calculator for vector operations."""

    @staticmethod
    def validate_vector(func):
        """Validate that two vectors have the same size.

        Args:
            func (function): Function to validate.

        Returns:
            function: Wrapped function with vector size validation.
        """

        def wrapper(v1, v2, *args, **kwargs):
            """Validate vector sizes before calling the function.

            Args:
                v1 (list): First vector.
                v2 (list): Second vector.
                *args: Additional positional arguments.
                **kwargs: Additional keyword arguments.

            Returns:
                Any: Result returned by the wrapped function.

            Raises:
                ValueError: If the vectors have different sizes.
            """
            if len(v1) != len(v2):
                raise ValueError("Vectors size doesn't match")
            return func(v1, v2, *args, **kwargs)

        return wrapper

    @staticmethod
    @validate_vector
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.
        """
        product = 0
        for i in range(len(V1)):
            product += V1[i] * V2[i]
        print("Dot product is:", product)

    @staticmethod
    @validate_vector
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors and print the resulting vector.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.
        """
        vec = []
        for i in range(len(V1)):
            vec.append(float(V1[i] + V2[i]))
        print("Add Vector is :", vec)

    @staticmethod
    @validate_vector
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract the second vector from the first and print the result.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.
        """
        vec = []
        for i in range(len(V1)):
            vec.append(float(V1[i] - V2[i]))

        print("Sous Vector is:", vec)