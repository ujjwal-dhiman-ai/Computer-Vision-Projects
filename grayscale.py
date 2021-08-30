# image color changer

import cv2

img = cv2.imread("C:\\Users\\LENOVO\\Desktop\\me.png",0)
img = cv2.resize(img,(600,600))
# print(img)
img = cv2.flip(img,1)
cv2.imshow('original',img)

k = cv2.waitKey(0)
if k==ord('s'):
    cv2.imwrite("C:\\Users\\LENOVO\\Desktop\\bw_me.png",img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()

# cv2.destroyAllWindows()