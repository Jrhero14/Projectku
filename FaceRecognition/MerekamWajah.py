import cv2, os, numpy as np
from PIL import Image
################################### IMPORT
cam = cv2.VideoCapture(0)
cam.set(3, 1080)
cam.set(4, 880)
DetectorWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
NamaWajah = input('Masukan Namamu: ')
FaceID = input('Masukan ID-Mu: ')
print("Sedang diproses Tunggu sebentar")
ambilData = 1
###################################Variabel
os.mkdir('DataBaseWajah/'+NamaWajah)
while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1)
    CamAbuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Faces = DetectorWajah.detectMultiScale(CamAbuAbu, 1.15, 5)
    for (x, y, w, h) in Faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        namaFile = 'wajah.'+str(FaceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite('DataBaseWajah/'+NamaWajah+'/'+namaFile, frame)
        ambilData += 1

    if ambilData > 100:
        break


wajahDir = 'DataBaseWajah/'+NamaWajah
latihDir = 'latihanwajah/'+NamaWajah
def getImageLabel(path):
    ImagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    faceIDs = []
    for ImagePath in ImagePaths:
        PILImg = Image.open(ImagePath).convert('L')
        imgNum = np.array(PILImg, 'uint8')
        faceID = int(os.path.split(ImagePath)[-1].split(".")[1])
        faces = DetectorWajah.detectMultiScale(imgNum)
        for (x,y,w,h) in faces:
            faceSamples.append(imgNum[y:y+h,x:x+w])
            faceIDs.append(faceID)
        return  faceSamples, faceIDs

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
DetectorWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print("sedang melakukan training data wajah")
faces,IDs = getImageLabel(wajahDir)
faceRecognizer.train(faces,np.array(IDs))

faceRecognizer.write(latihDir+'training.xml')
print("Sebanyak {0} data wajah telah ditraining ke mesin", format(len(np.unique(IDs))))

print("Deteksi wajah Selesai")
cam.release()
cv2.destroyAllWindows()
