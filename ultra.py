import serial
import time
import cv2
import requests
import matplotlib.pyplot as plt

import cv2
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(0)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    
    return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
while(1):
    for i in range(ramp_frames):
        temp = get_image()
    print("Taking image...")
# Take the actual image we want to keep
    camera_capture = get_image()
    #cv2.imshow('a', camera_capture)

    file = "test_image.png"
    cv2.imwrite(file, camera_capture)
    url = 'http://35.203.172.8:8888/'
    files = {'media': open('test_image.png', 'rb')}
    a=requests.post(url, files=files)
    print(a.text)
    import serial
    import time

    ArduinoSerial = serial.Serial('/dev/ttyACM0',9600)
    time.sleep(2)
    y=a.text

    if y==1:
    		ArduinoSerial.write( b'1')
    else:
    		ArduinoSerial.write(b'0')
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!

 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)
