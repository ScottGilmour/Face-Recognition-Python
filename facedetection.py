import numpy as np
import cv2

print 'Loading image'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
test = face_cascade.load('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
print(test)


img = cv2.imread('test2.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print 'Loaded image, applying cascade classifiers'

faces = face_cascade.detectMultiScale(grayimg, 1.3, 5)

for (x, y, w, h) in faces:
	img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	roi_gray = grayimg[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	
imgResized = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.imshow('Face Detection', imgResized)
cv2.waitKey(0)
cv2.destroyAllwindows()


