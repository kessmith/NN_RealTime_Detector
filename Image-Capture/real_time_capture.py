import cv2
import os
import time
############################################
myPath = 'data/images'
imgWidth = 780
imgHeight = 540
moduleVal = 10
saveImg = True
showImage = True
############################################

cap = cv2.VideoCapture(0)

index = 0
countFolder = 0
countSave = 0

def saveData():
    global countFolder
    countFolder = 0
    while os.path.exists(myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath+ str(countFolder))


# We need to add in logic to check if path already exist
if saveImg:
    saveData()
    
while 1:
    saveCount = 0
    success, img = cap.read()
    img = cv2.resize(img, (imgWidth, imgHeight), interpolation=cv2.INTER_LINEAR)
    
    if saveData:
        if index % moduleVal == 0:
            nowTime = time.time()
            cv2.imwrite(myPath + str(countFolder) + '/' + 'image' + '_' + str(saveCount) + str(nowTime) +".jpg", img)
        saveCount +=1
    index +=1
    
    if showImage:
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cap.destroyAllWindows()