import cv2

filename = "img.png"

# creat a HOGDescriptor object
hog = cv2.HOGDescriptor()
# Intitial the pepole Detector in image
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# load image
image = cv2.imread(filename)

# detect people
# image: source image
# winSride:step size in x and y direction of sliding window
# padding :no. od pixels in x and y direction for padding of sliding window
# Scale : Detection window size increase people
# bounding boxes : location of detection people
# wights : wight scores of detected people

(bounding_boxes,weights)=hog.detectMultiScale(image,
                                              winStride=(4,4),
                                              padding=(8,8),
                                              scale=1.05)
#Draw bounding boxes on the image
for (x,y,w,h) in bounding_boxes:
    cv2.rectangle(image,
                  (x,y),
                  (x+w,y+h),
                  (0,0,255),
                  4)
size =len(filename)
new_filename=filename[:size-4]
new_filename=new_filename+"_detect.png"
# cv2.imwrite(new_filename,image)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()