import cv2 as cv
import numpy as np

# canvas = cv.imread(r"C:\Users\LENOVO\Downloads\monolith.jpg")
# canvas = cv.resize(canvas,(1024,512))
canvas = np.ones((512,1024),np.uint8)
print(canvas)

canvas = cv.line(canvas,(0,0),(200,200),(125,246,20),5)
canvas = cv.line(canvas,(200,200),(400,0),(125,246,20),5)
canvas = cv.arrowedLine(canvas,(200,200),(200,400),(125,246,20),5)
canvas = cv.rectangle(canvas,(100,400),(300,500),(125,246,20),5)
canvas = cv.circle(canvas, (200,100),50,(150,150,150),5)

font = cv.FONT_HERSHEY_COMPLEX
canvas = cv.putText(canvas,"I am learning Computer Vision", (250,200), font, 1.2,(200,200,200),2,cv.LINE_AA)

canvas = cv.ellipse(canvas, (450,350),(100,50),0,0,360,0,5)
#canvas1 = np.ones((512,1024),np.uint8) # black canvas
#print(canvas1)
cv.imshow("canvas",canvas)
cv#.imshow("canvas1",canvas1)
cv.waitKey(0)
cv.destroyAllWindows()