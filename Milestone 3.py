import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

min_size = 3
max_size = 21
current_size = min_size
blur_dir = 2

while(True):
    ret, frame = cap.read()
    if ret == True:
        # Blurring the image
        kernel_size = (current_size, current_size)
        blurred_frame = cv2.GaussianBlur(frame, kernel_size, 0)
        # Updating the blur amount
        current_size += blur_dir
        if current_size > max_size or current_size < min_size:
            blur_dir *= -1
        # Displaying the blurred frame
        cv2.imshow('Webcam', blurred_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()