import cv2

img = cv2.imread("C:\\Users\\LENOVO\\Desktop\\me.png",1)
img = cv2.resize(img,(600,600))
print(img)

cv2.imshow('original',img)

# img = cv2.imread("C:\\Users\\LENOVO\\Desktop\\me.png",0)
# img = cv2.resize(img,(600,600))
# print(img)

# cv2.imshow('grayscale',img)

cv2.waitKey(0)

cv2.destroyAllWindows()