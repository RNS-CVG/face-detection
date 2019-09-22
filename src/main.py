from face_detect import image_detect,camera_detect,video_detect
import cv2
import sys
import argparse


#intorducing command line using parse_args
parser = argparse.ArgumentParser()
parser.add_argument("par", help="enter 1 for image detection 2 for camera capture and 3 for video file face detection",type=int)
args = parser.parse_args()


if(args.par==1):
    img = cv2.imread("goldberg.jpg")

    image_detect(img) #passing image as argument
elif(args.par==2):

    camera_detect() #camera face detection
else:
    video_capture = cv2.VideoCapture("sample.mp4")
    video_detect(video_capture) #passing video as argument
