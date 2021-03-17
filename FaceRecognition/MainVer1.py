import cv2, os
################################### IMPORT
cam = cv2.VideoCapture(0)
cam.set(3, 1080)
cam.set(4, 880)
DetectorWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
###################################Variabel

###################################Fungsi

while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1)
    CamAbuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Faces = DetectorWajah.detectMultiScale(CamAbuAbu, 1.15, 5)
    for (x, y, w, h) in Faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow("WebCam", frame)
    #cv2.imshow("WebCam Abu-Abu", CamAbuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
print("Deteksi wajah Selesai")
cam.release()
cv2.destroyAllWindows()