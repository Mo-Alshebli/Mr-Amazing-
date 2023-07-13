import matplotlib.pyplot as plt
import cv2
img1=cv2.imread("img1.png")
img2=cv2.imread("img2.png")

orb=cv2.ORB_create()

kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches=bf.match(des1,des2)
print(len(matches))
matches=sorted(matches,key=lambda x:x.distance)

img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
cv2.imshow("Keypoint",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()