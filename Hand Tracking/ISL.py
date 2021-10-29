import cv2
import time
import numpy as np
import Hand_Tracking_module as htm
import math

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime=0
detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList) != 0:

        Tx, Ty = lmList[4][1], lmList[4][2]
        Ix, Iy = lmList[8][1], lmList[8][2]
        Sx, Sy = lmList[20][1], lmList[20][2]
        M4x ,M4y = lmList[9][1], lmList[9][2]
        Mx, My = lmList[12][1], lmList[12][2]
        Px, Py = lmList[0][1], lmList[0][2]

        INTH=math.hypot(Ix-Tx, Iy-Ty)
        M4TH=math.hypot(M4x-Tx, M4y-Ty)
        MI= math.hypot(Mx-Ix, My-Iy)
        MP=math.hypot(Mx-Px, My-Py)
        # print(MI)

        if (INTH>=250):
            cv2.putText(img, "L", (320, 240), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))

        if (INTH>=40 and INTH<=100 and MI>=100 and MI<=150):
            cv2.putText(img, "C", (320, 240), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))

        if (M4TH>=0 and M4TH<=10):
            cv2.putText(img, "B", (320, 240), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))

        if (MP>=50 and MP<=80):
            cv2.putText(img, "A", (320, 240), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}' , (450,50), cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)