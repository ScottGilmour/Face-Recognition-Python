import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

print 'Image detection, Scott Gilmour, for Digital Attractions/Ryan Lemmex'
print 'https://github.com/ScottGilmour' 

print 'Loading cascade...'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
test = face_cascade.load('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
print(test)

dir = 'C:\images'

def applyCascade( image_name ):
	img = cv2.imread(join(dir, image_name))
	grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	print 'Loaded ', file

	faces = face_cascade.detectMultiScale(grayimg, 1.3, 5)
	face_count = 0

	for (x, y, w, h) in faces:
		face_count = face_count + 1
		
	print 'Faces found: ', face_count

	return face_count

for (file) in listdir(dir):
	applyCascade(file)
	