import cv2

cap = cv2.VideoCapture(r"C:\Users\LENOVO\Downloads\motivation1.mp4")

count = 0
while True:
    ret, frame = cap.read()
    cv2.imwrite(r"E:\PRACTICE\OpenCV\frames\imgN%d.png"%count,frame)
    count += 1
    cv2.imshow("frames",frame)
    print("TO STOP SPLITING VIDEO INTO FRAMES PRESS 'q'")
    if cv2.waitKey(10) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
