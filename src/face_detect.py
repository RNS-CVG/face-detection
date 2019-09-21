import numpy as np
from cv2 import cv2

def image_detect():

    img = cv2.imread('media/images/sachin.jpg') 
    detect_faces(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def video_detect():

    cap = cv2.VideoCapture('media/videos/1.MP4')
    while(cap.isOpened()):
        ret,frame = cap.read()
        detect_faces(frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def cam_detect():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        detect_faces(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

    cap.release()
    cv2.destroyAllWindows()

def detect_faces(frame):
    face_cascade = cv2.CascadeClassifier('src/hf.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        gray = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('frame',gray)