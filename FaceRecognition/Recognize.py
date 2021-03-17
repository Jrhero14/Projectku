import cv2, os, numpy as np
################################### IMPORT
wajahDir = 'DataBaseWajah'
latihDir = 'latihanwajah/Jeremitraining.xml'

cam = cv2.VideoCapture(0)
cam.set(3, 1080)
cam.set(4, 880)
DetectorWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceRecognizer2 = cv2.face.LBPHFaceRecognizer_create()

faceRecognizer.read(latihDir)
faceRecognizer2.read('latihanwajah/Jokowitraining.xml')
Font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
names = ['tidak diketahui', 'Jeremi', 'Jokowi']

minWidth = 0.1*cam.get(3)
minHeigth = 0.1*cam.get(4)

while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1)
    CamAbuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Faces = DetectorWajah.detectMultiScale(CamAbuAbu, 1.15, 5, minSize=(round(minWidth), round(minHeigth)))

    for (x, y, w, h) in Faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        id, confidence = faceRecognizer.predict(CamAbuAbu[y:y+h, x:x+w])
        id2, confidence2 = faceRecognizer2.predict(CamAbuAbu[y:y + h, x:x + w])
        print(str(id)+'|'+str(confidence))
        print(str(id2) + '|' + str(confidence2))
        if (confidence < 35):
            nameID = names[id]
            confidenceTXT = "{0}%".format(round(100+confidence))
        elif (confidence > 40):
            nameID = names[2]
            confidenceTXT = "{0}%".format(round(100 + confidence))
        else:
            nameID = names[0]
            confidenceTXT = "{0}%".format(round(100 + confidence))
        cv2.putText(frame, str(nameID), (x+5,y-5),Font,1,(255,255,255), 2)
        cv2.putText(frame, str("{0}%".format(round(100 + confidence))), (x + 5, y+h-5), Font, 1, (255, 255, 0), 1)

    cv2.imshow("Recoginze", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

print("EXIT")
cam.release()
cv2.destroyAllWindows()