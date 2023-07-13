import cv2
import numpy as np
import tensorflow
import pandas as pd
import matplotlib.pyplot as plt
import imutils
import easyocr

img= cv2.imread("OIP.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))

bfilter=cv2.bilateralFilter(gray,11,17,17)
edged=cv2.Canny(bfilter,200,200)


keypoints,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


# keypoints=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for i in range(len(keypoints)):
    hull=cv2.convexHull(keypoints[i])
    cv2.drawContours(edged,[hull],-1,(55,220,30),2)
cv2.imshow("Gray",keypoints)
print(keypoints)
contourss=imutils.grab_contours(keypoints)
contours=sorted(contourss,key=cv2.contourArea,reverse=True)
# print(contours)

# print(contours)



location=None
for contour in contours:

    approx=cv2.approxPolyDP(contour,10,True)

    for i in range(len(approx)):
        print(approx[i][0])
        cv2.circle(edged, approx[i][0], 4, (125, 25, 255), -1)

        print("==========")
        for j in range(i):
            # print(approx[i][j])
            pass
            # cv2.circle(edged, approx[i][j], 4, (125, 25, 255), -1)

            # print()
    if len(approx)==3:
        print("jhkj")
        location=approx
        break
print(location[0][0])
cv2.circle(edged,location[0][0],4,(125,25,255),-1)
cv2.imshow("Gray",edged)


mask=np.zeros(gray.shape,np.uint8)
new_image=cv2.drawContours(mask,[location],0,255,-1)
new_image=cv2.bitwise_and(img,img,mask=mask)


(x,y)=np.where(mask==255)
(x1,y1)=(np.min(x),np.min(y))
(x2,y2)=(np.max(x),np.max(y))
cropped_image=gray[x1:x2+1,y1:y2+1]

reader=easyocr.Reader(['en'])
result=reader.readtext(cropped_image)

print(result)
text=result[0][-2]
font=cv2.FONT_HERSHEY_DUPLEX
res=cv2.putText(img,text=text,org=(approx[0][0][0],approx[1][0][1]+60),fontFace=font,fontScale=1,color=(0,255,0))
res=cv2.rectangle(img,tuple(approx[0][0]),tuple(approx[2][0]),(0,255,0),3)
# cv2.imshow("Gray",res)

cv2.waitKey(0)
print(text)

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# img = cv2.imread("3.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray)
# # coustom=r'--oem 3 --psm 6 lang=ara'
text = pytesseract.image_to_string(gray)
cv2.imshow("Gray",gray)

cv2.waitKey(0)
# print(text)