import cv2 as cv
import datetime

cap = cv.VideoCapture(0,cv.CAP_DSHOW)
print("Width--> ",cap.get(3))
print("Height--> ",cap.get(4))

while cap.isOpened():
    ret , frame = cap.read()
    
    if ret:
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height: ' + str(cap.get(4)) + '    Width: ' + str(cap.get(3))
        frame = cv.flip(frame,1)
        frame = cv.putText(frame, text, (10,20),font, 1,(0,120,0),1,cv.LINE_AA)
        date_data = 'Date and Time: ' + str(datetime.datetime.now())
        frame = cv.putText(frame,date_data, (10,50), font, 1, (255,100,255),1,cv.LINE_AA)
        cv.imshow('framw', frame)
        if cv.waitKey(25) == ord('q'):
            break
    else:
        break
        
cap.release()
cv.destroyAllWindows()