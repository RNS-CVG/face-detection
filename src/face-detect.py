import cv2
import sys

def detect_func():
    face_cascade = cv2.CascadeClassifier("h1.xml")
    eye_cascade = cv2.CascadeClassifier("h2.xml")
    
    x=int(input("Enter 1 for image,2 for camera capture and 3 for video file"))
    
    if(x==1):
        img = cv2.imread("goldberg.jpg") #reading the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting it to grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) #recognizing the face coordiantes in the image using the classifer
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #highlighting the face with a rectangle


        cv2.imshow('img',img) # displaying the image with a rectangle
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        sys.exit()
        
    if(x==2):
        video_capture = cv2.VideoCapture(0)
        
    if(x==3):
        video_capture = cv2.VideoCapture("sample.mp4")

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()

    cv2.destroyAllWindows()
