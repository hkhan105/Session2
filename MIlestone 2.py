import cv2
import numpy as np

# Load an image
video = cv2.VideoCapture(0)

# Get the dimensions of the image
rows, cols = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(video.get(cv2.CAP_PROP_FRAME_WIDTH))

# Define the angle of rotation
angle = 0

# Loop for each frame
while(True):
    # Read a frame from the video
    ret, frame = video.read()
    # Get the rotation matrix
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    # Rotate the image
    rotated_frame = cv2.warpAffine(frame, M, (cols, rows))
    # Display the rotated image
    cv2.imshow('Rotated Video', rotated_frame)
    # Increment the angle
    angle += 1
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break