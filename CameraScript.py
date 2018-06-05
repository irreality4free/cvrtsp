# --*-- coding:utf-8 --*--
import cv2 as cv
from datetime import datetime
import time

ADDR = "rtsp://admin:admin@10.2.6.4:554/1/h264major"
ADDR = "rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov"
DIR = "./video/"

class Camera:
    def __init__(self):
        self.stop_flag = False
        self.vcap = cv.VideoCapture(ADDR)

    def check_cam(self):

        if (self.vcap.isOpened()) == False:
            print('camera error')
        else:
            print('camera is ok')


    def record(self, name=False):

        frame_width = int(self.vcap.get(3))
        frame_height = int(self.vcap.get(4))

        self.check_cam()

        if not name:
            name = DIR + datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + '.avi'
        self.out = cv.VideoWriter(name, cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10.0,
                                  (frame_width, frame_height))  # name, codec, fps, frame size
        while True:
            # time.sleep(1)
            print('frame written')
            # ret, frame = self.vcap.read()
            # if ret == True:
            #     self.out.write(frame)
            #     if self.stop_flag:
            #         print('record stoped')
            #         self.stop_flag = False
            #         break



if __name__ == "__main__":
    cam = Camera()
    cam.record()