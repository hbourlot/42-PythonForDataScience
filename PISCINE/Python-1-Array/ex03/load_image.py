import numpy as np
import cv2 as cv


def ft_load(path: str) -> list:

    image = cv.imread(path)

    if image is None:
        raise ValueError("Couldn't load the image")

    print("The shape of image is: ", image.shape)

    return np.array(image)
