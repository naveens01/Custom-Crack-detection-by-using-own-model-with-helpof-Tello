from djitellopy import tello
import CrackDetection as cd
import cv2
import time


cd.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()


def getKeyBoardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if cd.getKey("LEFT"):
        lr = -speed
    elif cd.getKey("RIGHT"):
        lr = speed

    if cd.getKey("UP"):
        fb = speed
    elif cd.getKey("DOWN"):
        fb = -speed

    if cd.getKey("w"):
        ud = speed
    elif cd.getKey("s"):
        ud = -speed

    if cd.getKey("a"):
        yv = speed
    elif cd.getKey("d"):
        yv = -speed

    if cd.getKey("q"):
        me.land()
        # time.sleep(3)
    if cd.getKey("e"):
        me.takeoff()

    if cd.getKey('z'):
        cv2.imwrite(f'E:/tello/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True:
    vals = getKeyBoardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    cd.crackDet(img)
    cv2.waitKey(1)




