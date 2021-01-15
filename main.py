import cv2
import numpy as np

from matplotlib import pyplot as plt

# function(nothing to do)
def nothing(x):
    pass

#import image
img = cv2.imread('C:\\Users\\na-31\\Desktop\\2dan.jpg',0)
# #create and get Trackbar position
# cv2.createTrackbar('hreshold','hreshold',0,255,nothing)
# thre = cv2.getTrackbarPos('threshold','smoothing')
#
# #detect edge
# edges = cv2.Canny(img,thre,200)

#median
img = cv2.medianBlur(img,5)

edges = cv2.Canny(img,5,15)

#edge
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
