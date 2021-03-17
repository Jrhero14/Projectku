import cv2
import numpy as np
import math
import pygame as pg
from pygame import mixer
from playsound import playsound
import time
pg.init()
########################

cap = cv2.VideoCapture(0)
mx = 0
musicIndicator = 1

########################
# cap = cv2.VideoCapture(0)
# frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#
# frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
#
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#
# out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))
#
# ret, frame1 = cap.read()
# ret, frame2 = cap.read()
#
# while cap.isOpened():
#     diff = cv2.absdiff(frame1, frame2)
#     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5,5), 0)
#     _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
#     dilated = cv2.dilate(thresh, None, iterations=3)
#     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#
#     for contour in contours:
#         (x, y, w, h) = cv2.boundingRect(contour)
#         if cv2.contourArea(contour) > 700:
#             print("MALING")
#             mx += 1
#             cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
#                         1, (0, 0, 255), 2)
#     print(mx)
#     if (mx > 200):
#         mixer.music.load('Seram.mp3');
#         mixer.music.play()
#         time.sleep(5)
#         playsound('Kunti.mp3')
#         break
#     #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
#
#     image = cv2.resize(frame1, (1280,720))
#     out.write(image)
#     cv2.imshow("Camera", frame1)
#     frame1 = frame2
#     ret, frame2 = cap.read()
#
#     if cv2.waitKey(40) == 27:
#         break
#
# cv2.destroyAllWindows()
# cap.release()
# out.release()


while(1):

    try:  #an error comes if it does not find anything in window as it cannot find contour of max area
          #therefore this try error statement

        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)

        #define region of interest
        roi=frame[100:438, 100:538]


        cv2.rectangle(frame,(100,100),(538,438),(0,255,0),0)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)



    # define range of skin color in HSV
        lower_skin = np.array([0,20,70], dtype=np.uint8)
        upper_skin = np.array([20,255,255], dtype=np.uint8)

     #extract skin colur imagw
        mask = cv2.inRange(hsv, lower_skin, upper_skin)



    #extrapolate the hand to fill dark spots within
        mask = cv2.dilate(mask,kernel,iterations = 4)

    #blur the image
        mask = cv2.GaussianBlur(mask,(5,5),100)



    #find contours
        contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

   #find contour of max area(hand)
        cnt = max(contours, key = lambda x: cv2.contourArea(x))

    #approx the contour a little
        epsilon = 0.0005*cv2.arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epsilon,True)


    #make convex hull around hand
        hull = cv2.convexHull(cnt)

     #define area of hull and area of hand
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)

    #find the percentage of area not covered by hand in convex hull
        arearatio=((areahull-areacnt)/areacnt)*100

     #find the defects in convex hull with respect to hand
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)

    # l = no. of defects
        l=0

    #code for finding no. of defects due to fingers
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            pt= (100,180)


            # find length of all sides of triangle
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            s = (a+b+c)/2
            ar = math.sqrt(s*(s-a)*(s-b)*(s-c))

            #distance between point and convex hull
            d=(2*ar)/a

            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57


            # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
            if angle <= 90 and d>30:
                l += 1
                cv2.circle(roi, far, 3, [255,0,0], -1)

            #draw lines around hand
            cv2.line(roi,start, end, [0,255,0], 2)


        l+=1
        #######################################
        print(areahull)
        if (areahull > 5000):
            print("MALING")
            if (musicIndicator == 1):
                mixer.music.load('Sound.mp3')
                mixer.music.play(-1)
                musicIndicator = 0
        else:
            mixer.music.stop()
            musicIndicator = 1
            print(" ")
        cv2.imshow('mask', mask)
        cv2.imshow('frame', frame)


    except:
        pass

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()