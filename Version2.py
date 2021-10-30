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

count = 0
word = []
pword = " "
str = " "


def call(let):
    global pword
    if (pword != let):
        word.append(let)
        pword = let


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    cv2.line(img, (0, 400), (640, 400), (0, 0, 0), 3)

    pw = str.join(word)
    cv2.putText(img, pw, (50, 450),
                cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

    if len(lmList) != 0:

        Tx, Ty = lmList[4][1], lmList[4][2]
        Ix, Iy = lmList[8][1], lmList[8][2]
        Sx, Sy = lmList[20][1], lmList[20][2]
        M4x, M4y = lmList[9][1], lmList[9][2]
        Mx, My = lmList[12][1], lmList[12][2]
        Px, Py = lmList[0][1], lmList[0][2]
        I3x, I3y = lmList[6][1], lmList[6][2]
        Rx, Ry = lmList[16][1], lmList[16][2]

        INTH = math.hypot(Ix - Tx, Iy - Ty)
        M4TH = math.hypot(M4x - Tx, M4y - Ty)
        MI = math.hypot(Mx - Ix, My - Iy)
        MP = math.hypot(Mx - Px, My - Py)
        I3TH = math.hypot(I3x - Tx, I3y - Ty)
        RS = math.hypot(Rx-Sx, Ry-Sy)
        ST = math.hypot(Sx-Tx, Sy-Ty)
        MT = math.hypot(Mx-Tx, My-Ty)
        SI = math.hypot(Sx-Ix, Sy-Iy)
        MR = math.hypot(Mx-Rx, My-Ry)
        RI = math.hypot(Rx-Ix, Ry-Iy)
        print(MR)

        if (I3TH >= 150 and I3TH <= 200):  # backspace
            count = count + 1
            if (len(word) != 0):
                if count > 25:
                    word.pop()
                    pword = " "
                    count = 0

        if (INTH >= 250):
            count = count + 1
            if count > 20:
                let = "L"
                count = 0
                call(let)

        if (INTH >= 40 and INTH <= 100 and MI >= 100 and MI <= 150):
            count = count + 1
            if count > 20:
                let = "C"
                count = 0
                call(let)

        if (M4TH >= 0 and M4TH <= 10):
            count = count + 1
            if count > 20:
                let = "B"
                count = 0
                call(let)

        if (MP >= 50 and MP <= 80):
            count = count + 1
            if count > 20:
                let = "A"
                count = 0
                call(let)

        # if (ST >= 90 and ST <= 110):
        #     count = count + 1
        #     if count > 20:
        #         let = "D"
        #         count = 0
        #         call(let)

        if (ST >= 20 and ST <= 40):
            count = count + 1
            if count > 20:
                let = "E"
                count = 0
                call(let)

        if (INTH >= 0 and INTH <= 30):
            count = count + 1
            if count > 20:
                let = "F"
                count = 0
                call(let)

        if (MT >= 100 and MT <= 130 and INTH >= 120 and INTH <= 140):
            count = count + 1
            if count > 20:
                let = "G"
                count = 0
                call(let)

        if (MT >= 150 and MT <= 190 and INTH >= 140 and INTH <= 200):
            count = count + 1
            if count > 20:
                let = "H"
                count = 0
                call(let)

        if (RS >= 160 and RS <= 200):
            count = count + 1
            if count > 20:
                let = "I"
                count = 0
                call(let)

        if (INTH >= 60 and INTH <= 90 and MI >= 100 and MI <= 130):
            count = count + 1
            if count > 20:
                let = "K"
                count = 0
                call(let)

        # if (INTH >= 80 and INTH <= 100):
        #     count = count + 1
        #     if count > 20:
        #         let = "M"
        #         count = 0
        #         call(let)

        # if (INTH >= 70 and INTH <= 80):
        #     count = count + 1
        #     if count > 20:
        #         let = "N"
        #         count = 0
        #         call(let)

        if (INTH >= 25 and INTH <= 45 and MI >= 0 and MI <= 30):
            count = count + 1
            if count > 20:
                let = "0"
                count = 0
                call(let)

        if (ST >= 370 and ST <= 400):
            count = count + 1
            if count > 20:
                let = "Y"
                count = 0
                call(let)

        if (SI >= 130 and SI <= 150):
            count = count + 1
            if count > 20:
                let = "X"
                count = 0
                call(let)

        if (MR >= 70 and MR <= 90):
            count = count + 1
            if count > 20:
                let = "W"
                count = 0
                call(let)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (450, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
