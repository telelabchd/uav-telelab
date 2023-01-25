# import necessary libs
import uvicorn, asyncio, cv2
from vidgear.gears.asyncio import WebGear
from vidgear.gears.asyncio.helper import reducer
import sys
import zmq
import base64
import numpy as np
from FrameConsumer import FrameConsumer

# initialize WebGear app without any source
web = WebGear(logging=True)

consumer = FrameConsumer("5562")
consumer.connect()

# activate jpeg encoding and specify other related parameters


# create your own custom frame producer
async def my_frame_producer():
    # initialize global params
    # Define NetGear Client at given IP address and define parameters
    # !!

    while True:
        # receive frames from network
        #frame = self.client.recv()
        frame = consumer.recv()
        # if NoneType
        if frame is None:
            break

        # do something with your OpenCV frame here

        # reducer frames size if you want more performance otherwise comment this line
        #frame = await reducer(
        #    frame, percentage=30, interpolation=cv2.INTER_AREA
        #)  # reduce frame by 30%

        # handle JPEG encoding
        encodedImage = cv2.imencode(".jpg", frame)[1].tobytes()
        # yield frame in byte format
        yield (b"--frame\r\nContent-Type:image/jpeg\r\n\r\n" + encodedImage + b"\r\n")
        await asyncio.sleep(0)
    # close stream
    #client.close()


# add your custom frame producer to config with adequate IP address
web.config["generator"] = my_frame_producer
try:
# run this app on Uvicorn server at address http://localhost:8000/
    uvicorn.run(web(), host="192.168.100.143", port=9091)
except KeyboardInterrupt:
# close app safely
    print("############################ Web Server Going Down#############")
    web.shutdown()
    sys.exit()
