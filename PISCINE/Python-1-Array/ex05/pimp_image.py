import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def ft_invert(image: list) -> list:
    """Invert pixels.

    Args:
        image (list): Array of an image.

    Returns:
        list: Inverted image.
    """
    h = len(image)
    w = len(image[0])
        
    invert = [[[] for _ in range(w)] for _ in range(h)]

    max_color = 255

    for i in range(h):
        for j in range(w):
            invert[i][j] = max_color - image[i][j]

    return invert


def ft_red(image) -> list:
    """Convert pixels to red.

    Args:
        image (list): Array of an image.

    Returns:
        list: Red image.
    """
    red = np.zeros_like(image)
    
    red[:, :, 0] = image[:, :, 0]
    
    return red


def ft_green(image: list) -> list:
    """Convert pixels to Green.

    Args:
        image (list): Array of an image.

    Returns:
        list: Green image.
    """
    green = np.zeros_like(image)
    
    green[:, :, 1] = image[:, :, 1]

    return green

def ft_blue(image: list) -> list:
    """Convert pixels to Blue.

    Args:
        image (list): Array of an image.

    Returns:
        list: Blue image.
    """
    blue = np.zeros_like(image)
    
    blue[:, :, 2] = image[:, :, 2]
    
    return blue


def ft_grey(image: list) -> list:
    """Convert pixels to grey.

    Args:
        image (list): Array of an image.

    Returns:
        list: Grey image.
    """
    r = image[:, :, 0] / 3
    g = image[:, :, 1] / 3
    b = image[:, :, 2] / 3

    value = (r + g + b).astype(int)

    grey = np.stack([value, value, value], axis=2)

    return grey
