import cv2
import numpy as np
image = "SampleImages/chicago.jpg"
def find_edges(image):
    """Finds edges in an image using Sobel and Canny edge detection.

    Args:
        image: The image to process.

    Returns:
        A tuple containing the Sobel and Canny edge images.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sobel edge detection
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    abs_grad_x = cv2.convertScaleAbs(sobelx)
    abs_grad_y = cv2.convertScaleAbs(sobely)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    # Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the image
    cv2.imshow('Sobel Edges', grad)
    cv2.imshow('Canny Edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return grad, edges