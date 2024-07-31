import cv2
import numpy as np

image = "SampleImages/wildColumbine.jpg"

def thresholding(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Apply morphological filters
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range of HSV values for the ball
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply morphological filters on the HSV image
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Use the mask to create a new image with only the ball
    result = cv2.bitwise_and(image, image, mask=mask)

    # Show the results
    cv2.imshow('Original', image)
    cv2.imshow('Gray', gray)
    cv2.imshow('Threshold', thresh)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()