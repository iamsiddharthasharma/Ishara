import cv2
import time
import numpy as np
import Hand_Tracking_module as htm
import math

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

        Tx, Ty = lmList[4][1], lmList[4][2]
        Ix, Iy = lmList[8][1], lmList[8][2]
        Sx, Sy = lmList[20][1], lmList[20][2]
        M4x, M4y = lmList[9][1], lmList[9][2]
        Rx, Ry = lmList[16][1], lmList[16][2]
        Mx, My = lmList[12][1], lmList[12][2]
        Px, Py = lmList[0][1], lmList[0][2]

        INTH = math.hypot(Ix-Tx, Iy-Ty)
        M4TH = math.hypot(M4x-Tx, M4y-Ty)
        MI = math.hypot(Mx-Ix, My-Iy)
        MP = math.hypot(Mx-Px, My-Py)
        # Small finger thumb distance
        ST = math.hypot(Sx-Tx, Sy-Ty)
        MT = math.hypot(Mx-Tx, My-Ty)
        RS = math.hypot(Rx-Sx, Ry-Sy)
        print(RS)

        if (INTH >= 250):
            cv2.putText(img, "L", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (INTH >= 40 and INTH <= 100 and MI >= 100 and MI <= 150):
            cv2.putText(img, "C", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (M4TH >= 0 and M4TH <= 10):
            cv2.putText(img, "B", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (ST >= 90 and ST <= 110):
            cv2.putText(img, "D", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (ST >= 20 and ST <= 40):
            cv2.putText(img, "E", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (MP >= 50 and MP <= 80):
            cv2.putText(img, "A", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (INTH >= 30 and INTH <= 60):
            cv2.putText(img, "F", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (MT >= 10 and MT <= 40 and INTH >= 140 and INTH <= 200):
            cv2.putText(img, "G", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (MT >= 130 and MT <= 200 and INTH >= 140 and INTH <= 200):
            cv2.putText(img, "H", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

        if (RS >= 160 and RS <= 200):
            cv2.putText(img, "I", (400, 450),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (450, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
