import cv2
import numpy as np

from matplotlib import pyplot as plt

# function(nothing to do)
def nothing(x):
    pass
cv2.namedWindow('image')
#import image
img = cv2.imread('C:\\Users\\na-31\\Desktop\\2dan.jpg',0)
# #create Trackbars
cv2.createTrackbar('med_ksize','image',2,10,nothing)
cv2.createTrackbar('th_min','image',5,255,nothing)
cv2.createTrackbar('th_max','image',15,255,nothing)
beforemed= 5
before1 = 5
before2 = 15
firestflag = 1

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


    thre1 = cv2.getTrackbarPos('th_min','image')
    thre2 = cv2.getTrackbarPos('th_max','image')
    medksize = 2*(cv2.getTrackbarPos('med_ksize','image')) + 1

    print(thre1)
    print(thre2)
    print(medksize)

    if before1 != thre1 or before2 != thre2 or beforemed != medksize or firestflag == 1:
        before1 = thre1
        before2 = thre2
        beforemed = medksize
        firestflag = 0

        # median
        img_med = cv2.medianBlur(img, medksize)

        #detect edge
        edges = cv2.Canny(img_med,thre1,thre2)
        mededges = cv2.medianBlur(edges, 1)
        # edges = cv2.Canny(img,5,15)

        #edge
        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(mededges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()


cv2.destroyAllWindows()
