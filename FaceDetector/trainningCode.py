import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'FaceDetector/dataSet'

def getImagesWithID(img_path):
    imagePaths = [os.path.join(img_path, f) for f in os.listdir(img_path)]
    faces_list = []
    IDs = []

    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        #name = int(os.path.split(imagePath)[-1].split('.')[0])
        faces_list.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)
    return np.array(IDs), faces_list


Ids, faces = getImagesWithID(path)
recognizer.train(faces, Ids)   # train data or images with lbph algo
recognizer.save('FaceDetector/recognizer/trainningData.yml') 
cv2.destroyAllWindows()

