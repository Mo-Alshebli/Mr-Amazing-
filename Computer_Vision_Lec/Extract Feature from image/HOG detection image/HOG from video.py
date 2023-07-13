import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

filename="Street view with people walking in the Philippines.mp4"
file_size=(1920,1080)
output_filename="pedestraind_on_street.mp4"
output_frame_per_sec=20.0

# creat a HOGDescriptor object
hog = cv2.HOGDescriptor()
# Intitial the pepole Detector in image
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap=cv2.VideoCapture(filename)

fourcc=cv2.VideoWriter_fourcc(*"mp4v")
resulte=cv2.VideoWriter(output_filename,fourcc,output_frame_per_sec,file_size)

while cap.isOpened():
    success,frame=cap.read()

    if success:
        orig_frame=frame.copy()

        # detect people
        # image: source image
        # winSride:step size in x and y direction of sliding window
        # padding :no. od pixels in x and y direction for padding of sliding window
        # Scale : Detection window size increase people
        # bounding boxes : location of detection people
        # wights : wight scores of detected people

        (bounding_boxes, weights) = hog.detectMultiScale(orig_frame,
                                                         winStride=(4, 4),
                                                         padding=(8, 8),
                                                         scale=1.05)
        # Draw bounding boxes on the image
        for (x, y, w, h) in bounding_boxes:
            cv2.rectangle(orig_frame,
                          (x, y),
                          (x + w, y + h),
                          (0, 0, 255),
                          4)

        bounding_boxes=np.array([[x,y,x+w,y+h] for (x,y,w,h) in bounding_boxes])

        selection=non_max_suppression(bounding_boxes)

        for (x1,y1,x2,y2)in selection:
            cv2.rectangle(frame,
                          (x1,y1),
                          (x2,y2),
                          (0,255,0),
                          4)
        resulte.write(frame)
        cv2.imshow("Frame",frame)
        if cv2.waitKey(30)=="q":
            break
    else:
        break

cap.release()
resulte.release()
cv2.destroyAllWindow()

