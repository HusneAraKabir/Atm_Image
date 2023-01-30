import cv2
import serial
import numpy as np




def findName():
    filehandeler = open("FaceDetector/NameAndIdList.txt", "r")
    nameIdList = filehandeler.read()
    filehandeler.close()

    nameDictionary = {}

    nameArray = nameIdList.split(',')
    for i in nameArray:
        person = i.split(':')
        try:
            nameDictionary[int(person[0])] = person[1]
        except:
            continue
    
    return nameDictionary



def RecogniseImage(c_num):
    result = False
    name = "Unknown"
    numOfFrame = 1

    faceDetect = cv2.CascadeClassifier('FaceDetector/haarcascade/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("FaceDetector/recognizer/trainningData.yml")
    id = 0
    nameDictionary = findName()

    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (11, 102, 35), 2)
            id, conf = rec.predict(gray[y:y + h, x:x + w])   #  lbph use for prediction
            # cv2.putText(img,str(id), (x,y+h),font, (255,255,255))

            # if len(nameDictionary) != 0:
            #     name = nameDictionary[id]
            # else:
            #     name = "Unknown"


            if conf <= 40:
                name = "Found"
                cv2.putText(img, name, (x, y + h), cv2.FONT_ITALIC, 1, (255, 255, 255), 6, cv2.LINE_8)

            else:
                name = "Unknown"
                cv2.putText(img, "Unknown", (x, y + h), cv2.FONT_ITALIC, 1, (255, 255, 255), 6)

        cv2.imshow("Face", img)

        numOfFrame += 1

        if name == "Found":
            result = True
            break

        if numOfFrame == 500:
            break

        if (cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == ord('Q')):
            break


    cam.release()
    cv2.destroyAllWindows()
    return result


