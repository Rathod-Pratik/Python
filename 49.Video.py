import cv2
cam=cv2.VideoCapture('n.mkv')
while True:
    r,f=cam.read()
    cv2.imshow('video',f)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break;
cv2.destroyAllWindows()