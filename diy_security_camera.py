import cv2
import winsound

webcam = cv2.VideoCapture(0)

while True:
    _, image_one = webcam.read()
    _, image_two = webcam.read()
    frame_diff = cv2.absdiff(image_one,image_two)
    gray_diff = cv2.cvtColor(frame_diff,cv2.COLOR_BGR2GRAY)
    _, thresh_image = cv2.threshold(gray_diff,20,255,cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        winsound.Beep(500,100)

    cv2.imshow("Security Camera", thresh_image)

    if cv2.waitKey(10) == 27:
        break

webcam.release()
cv2.destroyAllWindows()