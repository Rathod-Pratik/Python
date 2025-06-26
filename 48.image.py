import cv2
# img=cv2.imread('SunShine.jpg',cv2.IMREAD_GRAYSCALE)  #Image style 
# img=cv2.imread('SunShine.jpg',cv2.IMREAD_UNCHANGED)  #Image style
img=cv2.imread('48.SunShine.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img, (300, 200)) 
g=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Title",g)
cv2.waitKey(0)
