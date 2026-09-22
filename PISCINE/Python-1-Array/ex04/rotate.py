import matplotlib.pyplot as plt
import cv2 as cv
from load_image import ft_load
import numpy as np

def main():
    """Load, crop, transpose, and display an image.
    """
    try:
        image = ft_load("animal.jpg")[1800:2200, 1300:1700]

        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        h = len(gray_image)
        w = len(gray_image[0])

        transpose = [[[] for _ in range(h)] for _ in range(w)]

        for i in range(h):
            for j in range(w):
                transpose[j][i] = gray_image[i][j]

        rotate = np.array(transpose)
        
        print("New shape after slicing: ", rotate.shape)
        print(rotate)

        plt.imshow(rotate, cmap="gray")
        plt.show()

    except Exception as error:
        print("Error:", error)

    

if __name__ == "__main__":
    main()
