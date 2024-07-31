import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    rows, cols, ch = frame.shape
    # Define the translation matrix
    # 1, 0, x
    # 0, 1, y
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    M = np.float32([[1, 0, x],[0, 1, y]])

    # Apply the transformation
    dst = cv2.warpAffine(frame,M,(cols,rows))

    # Display the resulting frame
    cv2.imshow('frame',dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
