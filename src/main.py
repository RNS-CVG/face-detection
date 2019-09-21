from face_detect import image_detect,video_detect,cam_detect
import sys
    
if sys.argv[0] == 1:
    image_detect()
elif sys.argv[0] == 2:
    video_detect()
else:
    cam_detect()
