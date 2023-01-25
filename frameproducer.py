import zmq
import random
import sys
import time
import cv2
import base64
import numpy as np


class FrameProducer:
    def __init__(self, port: str):
        self.port = port
        self.socket = None

    def connect(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.connect('tcp://192.168.100.143:'+self.port)

    def send(self, frame):
        frame = cv2.resize(frame, (640, 480))
        encoded, buffer = cv2.imencode('.jpg', frame)
        message = base64.b64encode(buffer)
        self.socket.send(message)
        #print("send")
