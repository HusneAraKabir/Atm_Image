import cv2


def makeUniqueID():
    filehandeler = open("FaceDetector/NameAndIdList.txt", "r")
    nameIdList = filehandeler.read()
    filehandeler.close()
    nameArray = nameIdList.split(',')

    return 1000+len(nameArray) #---- Starts from 1000


def RegisterImage(name):
    faceDetect = cv2.CascadeClassifier('FaceDetector/haarcascade/haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)

    # name = input('Enter Name: ')




    #id = int(input('enter Id: '))
    id = makeUniqueID()

    nameIdList = str(id) + ":" + name + ","

    filehandeler = open("FaceDetector/NameAndIdList.txt", "a")
    filehandeler.write(nameIdList)
    filehandeler.close()

    sampleNum = 0

    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1
            # cv2.imwrite("FaceDetector/dataSet/"+name+"("+str(sampleNum)+")"+"."+id+".jpg",gray[y:y+h,x:x+w])
            cv2.imwrite("FaceDetector/dataSet/" + name + "." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.waitKey(100)
        cv2.imshow("Face", img)
        cv2.waitKey(1)
        if (sampleNum >= 25):
            break

    cam.release()
    cv2.destroyAllWindows()

    import FaceDetector.trainningCode

