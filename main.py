import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()
    if ret:
        sobely = cv2.Sobel(back, cv2.CV_64F, 0, 1, ksize=5)
        laplacian = cv2.Laplacian(back, cv2.CV_64F)
        sobelx = cv2.Sobel(back, cv2.CV_64F, 1, 0, ksize=5)
        edges = cv2.Canny(back, 100, 100)
        cv2.imshow("image", edges)
        if cv2.waitKey(5) == ord("q"):
            cv2.imwrite("image.jpg", edges)
            cv2.imwrite("image_laplacian.jpg", laplacian)
            cv2.imwrite("image_sobelx.jpg", sobelx)
            cv2.imwrite("image_sobely.jpg", sobely)
            break
