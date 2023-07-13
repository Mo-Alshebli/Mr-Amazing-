import cv2

img=cv2.imread("img.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift=cv2.SIFT_create()
kp=sift.detect(gray)
img=cv2.drawKeypoints(gray,kp,None)

cv2.imshow("Keypoints",img)


imgi =cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoint with flags",imgi)

sift_=cv2.SIFT_create()
kp,des=sift_.detectAndCompute(gray,None)
imagg=cv2.drawKeypoints(gray,kp,imgi)
cv2.imshow("Keypoint with compute",imagg)

cv2.waitKey(0)
cv2.destroyAllWindows()