import numpy as np
import cv2 as cv


def ft_load(path: str) -> list:
    """Load an image from a file and display its shape.

    Args:
        path (str): Path to the image file.

    Raises:
        ValueError: If the image cannot be loaded.

    Returns:
        list: The loaded image as a NumPy array.
    """

    image = cv.imread(path)

    if image is None:
        raise ValueError("Couldn't load the image")

    print("The shape of image is: ", image.shape)

    return np.array(image)
