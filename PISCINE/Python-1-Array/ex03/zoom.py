import matplotlib.pyplot as plt
import cv2 as cv
from load_image import ft_load

def main():
    """Load, crop, and display a grayscale image.
    """
    try:
        image = ft_load("animal.jpg")
        print(image)

        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        zoomed = gray_image[1800:2200, 1300:1700]

        print("New shape after slicing: ", zoomed.shape)
        print(zoomed)

        plt.imshow(zoomed, cmap="gray")
        plt.show()

    except Exception as error:
        print("Error:", error)

    

if __name__ == "__main__":
    main()