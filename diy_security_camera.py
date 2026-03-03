import cv2
webcam = cv2.VideoCapture(0)
while True:
    _,im1 = webcam.read()
    cv2.imshow("Camera", im1)
    if cv2.waitKey(10) == 27:
        break
webcam.release()
cv2.destroyAllWindows()