import cv2

cap = cv2.VideoCapture(r"C:\Users\LENOVO\Downloads\motivation1.mp4")
print(cap)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("BW Motivation", gray)
    cv2.imshow("Arnold Motivation",frame)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
