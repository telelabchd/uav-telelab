import sys
import cv2
from FrameConsumer import FrameConsumer

port = "5560"
frameConsumer = FrameConsumer("5560")
frameConsumer.connect()

while True:
    frame = frameConsumer.recv()
    print(frame)

    #cv2.imshow("image", frame)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
#print ("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))
