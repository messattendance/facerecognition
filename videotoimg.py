import cv2
import time
cap=cv2.VideoCapture('http://192.168.2.69:8080/video')
#'http://192.168.43.1:8080/video'

count = 0
while True:
    ret,test_img=cap.read()
    if not ret :
        continue
    cv2.imwrite("train_img/abc1234/frame%d.jpg" % count, test_img)
    count += 1
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    
    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows
