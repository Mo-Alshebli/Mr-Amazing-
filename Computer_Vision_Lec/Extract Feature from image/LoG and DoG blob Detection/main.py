import matplotlib.pyplot as plt
import cv2

image=cv2.imread("img.png")

params=cv2.SimpleBlobDetector_Params()

params.minThreshold=0
params.maxThreshold=255

#filter by Area
params.filterByArea=True
params.minArea=50
params.maxArea=1000

#Filter by color(black=0)
params.filterByColor=False
params.blobColor=0

#Filter by Circularity
params.filterByCircularity=True
params.minCircularity=0.5
params.maxCircularity=1

# Filter by convexity
params.filterByConvexity=True
params.minConvexity=0.1
params.maxConvexity=2


# Setup the detector with parameters .
detector=cv2.SimpleBlobDetector_create(params)
keypoint=detector.detect(image)
print(" Number of blobs detected are : ",len(keypoint))
img_with_blobs=cv2.drawKeypoints(image,keypoint,None,(0,0,255))

plt.imshow(img_with_blobs)
cv2.imshow("Keypoint",img_with_blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()