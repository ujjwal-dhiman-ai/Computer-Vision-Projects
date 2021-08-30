import cv2 as cv
camera = "http://100.94.153.215:8080/video"
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
cap.open(camera)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('mobileoutput.mp4', fourcc, 20.0, (400, 600))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # frame = cv.flip(frame, 0)
    # write the flipped frame
    
    frame = cv.resize(frame,(400,600))
    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()