from flask import Flask
import cv2
from pip._vendor.requests.packages.urllib3.connectionpool import xrange
import base64
 
app = Flask(__name__)


@app.route('/take_image')
def takeImage():
    camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
    print('From sm2 project--------->>>going to take image ')
    camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
    def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = camera.read()
        return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
    for i in xrange(ramp_frames):
        temp = get_image()
    print("Taking image...")
# Take the actual image we want to keep
    camera_capture = get_image()
    file = "b7.png"

# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, camera_capture)
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
    print('going to return image')
    del(camera)

    encoded = base64.b64encode(open("b7.png", "rb").read())
    
    return encoded



if __name__ == '__main__':
    port = 9000 #the custom port you want
    app.run(host='0.0.0.0', port=port)