import cv2
# import os

img=cv2.imread("house.png")

fast=cv2.FastFeatureDetector_create()

keypoint=fast.detect(img,None)
img2=cv2.drawKeypoints(img,keypoint,None,color=(255,0,0))

print(" Threshold : ",format(fast.getThreshold()))
print("nonmaxsuppression: ",format(fast.getNonmaxSuppression()))
print("neighborhood: ",format(fast.getType()))
print(" total Keypoint with nonmaxsuooression: ",format(len(keypoint)))
# cv2.imshow("image_Fast",img2)
#able nonmaxsuppression
print("==============================================")
fast.setNonmaxSuppression(0)
keypoint=fast.detect(img,None)
print(" total Keypoint with nonmaxsuooression: ",format(len(keypoint)))
img3=cv2.drawKeypoints(img,keypoint,None,color=(255,0,0))
cv2.imshow("Nonmaxsuppression ",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
