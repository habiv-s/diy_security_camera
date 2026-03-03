import cv2
webcam = cv2.VideoCapture(0)
while True:
    _,im1 = webcam.read()
    _,im2 = webcam.read()
    diff = cv2.absdiff(im1,im2)
    cv2.imshow("Security Camera", diff)
    if cv2.waitKey(10) == 27:
        break
webcam.release()
cv2.destroyAllWindows()