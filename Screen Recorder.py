import cv2 as cv
import pyautogui as p
import numpy as np

rs = p.size()

fn = input("Please enter any file name and path")

fps = 20.0

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter(fn,fourcc,fps,rs)

cv.namedWindow("Live_Recording",cv.WINDOW_NORMAL)
cv.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv.cvtColor(f,cv.COLOR_BGR2RGB)
    cv.resize(f,(600,400))
    out.write(f)
    # cv.imshow("Live Recording",f)
    if cv.waitKey(1) == ord("q"):
        break
    
out.release()
cv.destroyAllWindows()