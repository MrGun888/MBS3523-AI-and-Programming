import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    width = cam.get(3) #column
    height = cam.get(4) #Row
    print(height,width)
    # frameResize = cv2.resize(frame, (400,400))
    # frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameBlur = cv2.GaussianBlur(frame, (15,15),0)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frameCanny = cv2.Canny(frame, 100, 200)
    cv2.imshow("Webcam", frame)
    # cv2.imshow("Webcam Resize", frameResize)
    # cv2.imshow("Webcam Gray", frameGray)
    cv2.imshow("Webcam HSV", frameHSV)
    cv2.imshow("Webcam Gaussian Blur", frameBlur)
    cv2.imshow("Webcam Canny Edges", frameCanny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()