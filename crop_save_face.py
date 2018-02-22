from PIL import Image
import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
img = cv2.imread('sajan.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))

d=0

# Draw a rectangle around the faces and crop face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 25), 2)
    cropped = img[y:y+h,x:x+w]
    filename = "cropped_%d.jpg"%d
    cv2.imwrite(filename,cropped)
    d+=1

cv2.imshow("Faces found" ,img)
cv2.waitKey(0)
