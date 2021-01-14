import cv2
import numpy as np
img2 = cv2.imread('C:\\Users\\na-31\\Pictures\\Huawei_novalite3\\photos\\flashair\\IMG_9268.JPG',1)
# img = np.full((512, 512, 3), 0, dtype=np.uint8)
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'Nana',(100,256),font,4,(255,255,255),2,cv2.LINE_AA)
# cv2.imshow('popup window', img)
height = img2.shape[0]
width = img2.shape[1]
img3 = cv2.resize(img2, (int(width*0.1), int(height*0.1)))
cv2.imshow('original', img2)
cv2.imshow('resize', img3)
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
cv2.waitKey(0)

