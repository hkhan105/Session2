import numpy as np
import cv2

origIm = cv2.imread('SampleImages/Coins/coins5.jpg')
imgray = cv2.cvtColor(origIm, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imgray, (5, 5), 0)
ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
contrs, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgray, contrs, -1, (0, 255, 0), 2)
for cntr in contrs:
    print(cv2.contourArea(cntr))
    (ulx, uly, wid, hgt) = cv2.boundingRect(cntr)
    cv2.rectangle(imgray, (ulx, uly), (ulx + wid, uly + hgt), (0, 0, 255), 2)
    convHull = cv2.convexHull(cntr)
    cv2.drawContours(imgray, [convHull], -1, (255, 255, 0), 1)
cv2.imshow('Contours', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()