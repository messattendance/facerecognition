import cv2
import time
cap=cv2.VideoCapture('http://192.168.2.69:8080/video')
#'http://192.168.43.1:8080/video'

count = 0
while True:
    ret,test_img=cap.read()
    if not ret :
        continue
<<<<<<< HEAD
    cv2.imwrite("train_img/1564Meenakshi/frame%d.jpg" % count, test_img)
=======
    cv2.imwrite("train_img/srinidhi/frame%d.jpg" % count, test_img)
>>>>>>> 1bd4015e43354c6b2f38dc5404f05c2d13003e8a
    count += 1
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    
    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows
