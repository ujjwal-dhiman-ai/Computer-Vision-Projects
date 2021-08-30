import cv2 as cv
import pafy

url = "https://www.youtube.com/watch?v=HlPkzdMP88Y&list=PLb0C_I-k2Ph_cidz6XgFkDaRyxjzQdSIK&index=1"

data = pafy.new(url)
data = data.getbest(preftype = "mp4")
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
cap.open(data.url)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('ytoutput.mp4', fourcc, 20.0, (600, 400))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # frame = cv.flip(frame, 0)
    # write the flipped frame
    
    frame = cv.resize(frame,(600,400))
    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(25) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()