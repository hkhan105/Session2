import cv2

cam = cv2.VideoCapture(0)
ret, prevFrame = cam.read()
prevGray = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)
while True:
    ret, currFrame = cam.read()
    currGray = cv2.cvtColor(currFrame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prevGray, currGray)
    # Apply thresholding to eliminate small movements and focus on larger objects
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    # Use morphing to fill in regions of movement
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Motion", thresh)
    x = cv2.waitKey(20)
    c = chr(x & 0xFF)
    if c == "q":
        break
    prevGray = currGray
cam.release()
cv2.destroyAllWindows()