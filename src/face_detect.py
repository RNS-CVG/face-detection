import numpy as np
from cv2 import cv2

def detect_function():

    face_cascade = cv2.CascadeClassifier('src/hf.xml')   #running the pretrained classifier
    img = cv2.imread('media/images/sachin.jpg') #reading the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting it to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #recognizing the face coordiantes in the image using the classifer
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #highlighting the face with a rectangle
        

    cv2.imshow('img',img) # displaying the image with a rectangle 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
