import cv2

img = cv2.VideoCapture(0)

ret, frame = img.read()

if ret == True:
    cv2.imwrite('foto.jpg', frame)

img.release()