import cv2, os, numpy as np
from PIL import Image

wajahDir = 'DataBaseWajah\Jeremi'
latihDir = 'latihanwajah/'
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













